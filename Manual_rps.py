import random
class RockPaperScissors:



    def __init__(self,rps):
        self.rps = rps
        
   
    def get_computer_choice(self):
        self.computer_choice = random.choice(rps)
        self.get_user_choice()

    def get_user_choice(self):
        self.user_choice = input("Choose rock, paper or scissors. ").lower()
        if self.user_choice not in self.rps:
            print("Please choose a valid option.")
        else:
            self.get_winner()
   
    def get_winner(self):
        print(f"You chose {self.user_choice}. The computer chose {self.computer_choice}.")
        
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



def play_game(rps):

    game = RockPaperScissors(rps)
    game.get_computer_choice()
    
if __name__ == '__main__':
    rps = ["rock","paper","scissors"]
    play_game(rps)
