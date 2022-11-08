import random
import time
import csv
import cv2
from keras.models import load_model
import numpy as np

class RPS:

    def __init__(self):
        self.cap = cv2.VideoCapture(0) # Open a camera for video capturing. To open default camera using default backend just pass 0.
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # construct a numpy array to read in data from image 224 x 224 pixels and 3 colour channels (RGB)
        self.model = load_model('keras_model.h5') #load model ready to make prediction
        self.moves = []
        self.computer_wins = 0
        self.user_wins = 0
        
    @staticmethod
    def get_countdown():
        print("Get ready to show your move!")
        countdown = 3
        while countdown > 0:
            minute, sec = divmod(countdown, 60)
            print(sec)
            cv2.waitKey(1000)
            countdown -= 1
            if countdown == 0:
                print("Show your move!") # checked  
    
    def get_labels(self):
        label_file = 'labels.txt'
        with open(label_file) as f:
            reader = csv.reader(f, delimiter=' ')
            label_dict = dict(reader)
            print(label_dict)
            for k, v in label_dict.items():
                self.moves.append(v)
                print(self.moves)
        return self.moves #checked: output is ['Rock', 'Paper', 'Scissors', 'Nothing']

    def get_computer_choice(self):
        computer_choice = random.choice(self.moves)
        print(computer_choice) #checked: output is a str of 1 of the elements in self.moves 
        print(type(computer_choice))
        return computer_choice

    def get_prediction(self):
        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image, ready to be read/used by tensorflow
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            prediction_index = np.argmax(prediction)
            print(prediction_index)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return prediction_index

    def get_user_choice(self, prediction_index):
        user_choice = self.moves[prediction_index]
        print(user_choice)
        return user_choice

    def get_winner(self, computer_choice, user_choice):
        print(computer_choice)
        print(user_choice)
        if computer_choice == user_choice:
            print(f"It's a tie! You both chose {computer_choice}.")
            winner = "It's a tie!"
        elif (computer_choice == "Rock" and user_choice == "Paper") or (computer_choice == "Paper" and user_choice == "Scissors") or (computer_choice == "Scissors" and user_choice == "Rock"):
            print(f"Congratulations! You won the game! You chose {user_choice} and the computer chose {categories_dict.get(computer_choice)}.")
            winner = "You won the game!"
        elif (computer_choice == "Rock" and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors" and user_choice == "Paper"):
            print(f"Oh no! You lost. Better luck next time! You chose {user_choice} and the computer chose {computer_choice}.")
            winner = "The computer won the game."
        else:
            print("I don't know what happened but none of the choices applied!")
            winner = "No winner."
        print(winner)
        return winner


def play():
    game = RPS()
    game.get_labels()
    prediction_index = game.get_prediction()
    computer_choice = game.get_computer_choice()
    game.get_countdown()
    user_choice = game.get_user_choice(prediction_index)
    game.get_winner(computer_choice, user_choice)
    # while comp or user wins is < 3 
    # run all methods in script 
    # if comp choice = 3, print user has lost

play()
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
    