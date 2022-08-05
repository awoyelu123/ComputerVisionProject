import random
from requests import options

class RockPaperScissors():
    def __init__(self,computer_choice,user_choice, get_winner):
        self.computer_choice = computer_choice
        self.user_choice = user_choice
        self.get_winner = get_winner
   
def get_computer_choice(self,rps_choice):
    self.rps_choice = ["rock","paper","scissors"]
    self.computer_choice = random.choice(rps_choice)

def get_user_choice(self):
    self.user_choice = input("Choose rock, paper or scissors. ").lower()
    self.user_choice not in self.rps_choice
   
def get_winner(self,computer_choice, user_choice):
    
    if self.computer_choice == "rock":
        if self.user_choice == "paper":
            print("You won!")
        elif self.user_choice == "rock":
            print("It is a draw!")
        else:
            print("You lost!")

    if self.computer_choice == "paper":
        if self.user_choice == "scissors":
            print("You won!")
        elif self.user_choice == "paper":
            print("It is a draw!")
        else:
            print("You lost!")


    if self.computer_choice == "scissors":
        if self.user_choice == "rock":
            print("You won!")
        elif self.user_choice == "scissors":
            print("It is a draw!")
        else:
            print("You lost!")



        
