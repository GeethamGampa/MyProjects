#============================== BANKING SYSTEM SIMULATION USING PYTHON AND OOPS ==============================# 

#------------------------- PROJECT DESCRIPTION -------------------------# 

# This project is a simple simulation of a banking system using 
# Object-Oriented Programming in Python. It allows users to create accounts, 
# deposit and withdraw money, check balances, and perform authentication using a PIN. 
# The system uses OOP principles like inheritance, encapsulation, and abstraction 
# to model different types of accounts (Savings and Current). This helps 
# demonstrate how real-world banking concepts can be implemented programmatically.

#------------------------- PROJECT OBJECTIVES -------------------------# 

# Learn and apply OOP concepts in a real-world scenario.
# Simulate essential banking operations like account creation, 
# balance checking, deposit, and withdrawal.
# Implement inheritance by modeling different account types.
# Practice encapsulation by protecting sensitive data like balance and PIN.

#------------------------- KEY FEATURES -------------------------#

# Create customer accounts (Savings or Current)
# Deposit money
# Withdraw money
# Check balance
# PIN-based authentication for security

#------------------------- OOPS CONCEPTS USED -------------------------#

# Class - Defined for Customer, Account, SavingsAccount, CurrentAccount
# Inheritance - SavingsAccount and CurrentAccount inherit from Account
# Encapsulation - Sensitive data like balance and PIN are kept private
# Abstraction - Account operations are grouped logically

#------------------------- TECHNOLOGIES USED -------------------------#

# Language : Python

#------------------------- CODE -------------------------#

class Customer:  # store customer info
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        
class Account:
    def __init__(self, customer, balance, pin):
        self.customer = customer
        self.__balance = balance
        self.__pin = pin
        
    def authenticate(self, pin):
        return self.__pin == pin
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"USD {amount} deposited. New balance: USD {self.__balance}")
        else:
            print("Invalid amount. Enter a valid positive amount.")
            
    def check_balance(self):
        print(f"Current Balance: USD {self.__balance}")
        
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Enter a valid positive amount.")
        elif amount <= self.__balance:
            self.__balance -= amount
            print(f"USD {amount} withdrawn. New balance: USD {self.__balance}")
        else:
            print("Insufficient balance!")
            
class SavingsAccount(Account):  # inherits from Account class
    def __init__(self, customer, balance, pin):
        super().__init__(customer, balance, pin)
        print(f"Savings Account created for {customer.name}")


class CurrentAccount(Account):  # inherits from Account class
    def __init__(self, customer, balance, pin):
        super().__init__(customer, balance, pin)
        print(f"Current Account created for {customer.name}")
            
#-----------Interactive Menu------------#
# interface

def main():
    print("Welcome to ABC Bank!")
    name = input("Enter your name: ")
    cid = input("Enter customer ID: ")
    from getpass import getpass
    pin = getpass("Set a 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return

    account_type = input("Choose account type (savings/current): ").lower()
    
    customer = Customer(name, cid)
    
    if account_type == "savings":
        account = SavingsAccount(customer, 0, pin)
    elif account_type == "current":
        account = CurrentAccount(customer, 0, pin)
    else:
        print("Invalid account type selected.")
        return
    
    # Authentication
    print(f"Welcome To Our Bank, {customer.name}")
    entered_pin = getpass("Enter your PIN: ")

    if not account.authenticate(entered_pin): 
        print("Authentication failed.")
        return
    
    # Operations menu
    while True:
        print("MENU")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter amount to deposit: "))
                account.deposit(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                amt = float(input("Enter amount to withdraw: "))
                account.withdraw(amt)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("GoodBye! Thank you for using ABC Bank!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

            