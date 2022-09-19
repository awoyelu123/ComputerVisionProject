import random
import cv2
from keras.models import load_model
import numpy as np
import time

def countdown(time_sec):

    while time_sec:
        mins, secs = divmod(time_sec,60)

        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

class RockPaperScissors:



    def __init__(self,rps, games_left = 3, computer_wins = 0, user_wins = 0):
        self.rps = rps
        self.games_left = games_left
        self.computer_wins = computer_wins
        self.user_wins = user_wins

        

    def get_computer_choice(self):
        self.computer_choice = random.choice(rps)
        self.get_prediction()



    def get_prediction(self):
        print("Please choose either rock, paper or scissors")
        countdown(5)
        print("Press Q to lock in your choice")
        model = load_model('keras_model1.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            self.max_index = np.argmax(prediction[0])
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
#cv2.puttext(frame,message,array)
        if self.max_index == 0:
            self.user_choice = "rock"
        elif self.max_index == 1:
            self.user_choice = "paper"
        elif self.max_index == 2:
            self.user_choice = "scissors"
        elif self.user_choice == 3:
            print("Please choose a valid option.")
            self.get_prediction()

        countdown(5)
        self.get_winner()

    def get_winner(self,):


        print(f"You chose {self.user_choice}. The computer chose {self.computer_choice}.")
        
        if self.computer_choice == "rock":
            if self.user_choice == "paper":
                print("You won!")
                self.user_wins += 1
                self.games_left -= 1
            elif self.user_choice == "rock":
                print("It is a draw!")
                self.games_left -= 1
            else:
                print("You lost!")
                self.computer_wins += 1
                self.games_left -= 1

        if self.computer_choice == "paper":
            if self.user_choice == "scissors":
                print("You won!")
                self.user_wins += 1
                self.games_left -= 1
            elif self.user_choice == "paper":
                print("It is a draw!")
            else:
                print("You lost!")
                self.computer_wins += 1
                self.games_left -= 1


        if self.computer_choice == "scissors":
            if self.user_choice == "rock":
                print("You won!")
                self.user_wins += 1
                self.games_left -= 1
            elif self.user_choice == "scissors":
                print("It is a draw!")
                self.games_left -= 1
            else:
                print("You lost!")
                self.computer_wins += 1
                self.games_left -= 1
        
        if self.user_choice == "nothing": 
            print("A choice was not entered.")




def play_game(rps):

    game = RockPaperScissors(rps,games_left=3, user_wins = 0, computer_wins = 0)
    game.get_computer_choice()

    while True:
        if game.games_left == 0:
            print (f"The game is over! You had {game.user_wins} wins. The computer had {game.computer_wins} wins.")
            if game.user_wins > game.computer_wins:
                print ("You won!")
            elif game.user_wins < game.computer_wins:
                print("The computer won!")
            else:
                print("Its a draw !")
            break
        else:
            print(f"You have {game.user_wins} wins, and the computer has {game.computer_wins} wins.")
            print(f"You have {game.games_left} game(s) left.")
            game.get_prediction()

if __name__ == '__main__':
    rps = ["rock","paper","scissors"]
    play_game(rps)
