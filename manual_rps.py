import random

categories = ["R", "P", "S"]
categories_dict = {"R": "ROCK", "P": "PAPER", "S": "SCISSORS"}


def get_computer_choice():
    computer_choice = random.choice(list(categories_dict))
    return computer_choice

def get_user_choice():
    user_choice = input("What move will you play: (R) rock, (P) paper or (S) scissors? [R/P/S]?\t")
    user_choice = user_choice.upper()
    if user_choice.upper() not in list(categories_dict):
        print("Oops! That is not a recognised move. Type a letter to pick a move: R (rock), P (paper) or S (scissors)?")
    return user_choice

def get_winner(computer_choice, user_choice):
    print(computer_choice)
    print(user_choice)
    if computer_choice == user_choice:
        print(f"It's a tie! You both chose {categories_dict.get(computer_choice)}.")
        winner = "It's a tie!"
    elif (computer_choice == "R" and user_choice == "P") or (computer_choice == "P" and user_choice == "S") or (computer_choice == "S" and user_choice == "R"):
        print(f"Congratulations! You won the game! You chose {categories_dict.get(user_choice)} and the computer chose {categories_dict.get(computer_choice)}.")
        winner = "You won the game!"
    elif (computer_choice == "R" and user_choice == "S") or (computer_choice == "P" and user_choice == "R") or (computer_choice == "S" and user_choice == "P"):
        print(f"Oh no! You lost. Better luck next time! You chose {categories_dict.get(user_choice)} and the computer chose {categories_dict.get(computer_choice)}.")
        winner = "The computer won the game."
    else:
        print("I don't know what happened but none of the choices applied!")
        winner = "No winner."
    return winner

def play():
    get_winner(get_computer_choice(), get_user_choice())

play()
