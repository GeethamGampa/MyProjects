#======================================= ROCK PAPER SCISSORS =======================================#


#----------------------------------- PROJECT DESCRIPTION -----------------------------------#

# Build a command-line version of the classic game Rock, Paper, Scissors 
# using Python and Object-Oriented Programming (OOP). The player competes 
# against the computer, and the game determines the winner based on standard rules. 

#----------------------------------- WHAT WE NEED -----------------------------------#

# Python(input, loops, if-else)
# OOP concepts:
# Class
# Object
# Method
# Encapsulation
# Random module (to let the computer make random choices)

#----------------------------------- WHAT WE NEED TO BUILD -----------------------------------#

# Break the project into 3 simple parts (classes):

# 1. Player class
# Gets user input: Rock, Paper, or Scissors.
# Handles invalid input.

# 2. Computer class
# Randomly chooses Rock, Paper, or Scissors using random.choice().

# 3. Game class
# Starts the game.
# Gets choices from both player and computer.
# Compares choices to decide the winner.
# Displays the result.

#----------------------------------- GAME FLOW -----------------------------------#
    
# Show instructions to the user.
# Ask the player to enter their move.
# Let the computer pick a random move.
# Compare both moves and decide the winner.
# Show the result.
# Ask if the player wants to play again. 

#----------------------------------- LEARNING GOALS -----------------------------------#

# Writing clean, modular code using classes
# Input handling and validation
# Using random for simple AI
# Comparing user and computer choices using logic
# Building and running a Python project

#----------------------------------- CODE -----------------------------------#

# Step 1: Create the Player class

class Player:
    def get_choice(self):
        choice = input("Enter Rock, Paper, or Scissors: ") 
        while choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid input. Please try again.")
            choice = input("Enter Rock, Paper, or Scissors: ") 
        return choice

# Step 2: Create the Computer class

import random

class Computer:
    def get_choice(self):
        return random.choice(["Rock", "Paper", "Scissors"])
    
# Step 3: Create the Game class

class Game:
    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def check_winner(self, player_choice, computer_choice):
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            return "It's a tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Paper" and computer_choice == "Rock") or
            (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            return "Yayyy! You won the game"
        else:
            return "Computer won! Better luck next time"

    def play(self):
        player_choice = self.player.get_choice()
        computer_choice = self.computer.get_choice()
        result = self.check_winner(player_choice, computer_choice)
        print(result)
        
# Step 4: Run the game

game = Game()
game.play()

# Step 5: Add Loop to Play Multiple Rounds 

while True:
    game = Game()
    game.play()
    
    again = input("\nDo you want to play again? (yes/no): ") 
    if again != "yes":
        print("Thanks for playing!")
        break






