import random

categories = ["R", "P", "S"]

# if user_input.upper() == "R":

# elif user_input.upper() == "P":
    
# elif user_input.upper() == "S":
# else:
#     print("Oops! That is not a recognised move. Type a letter to pick a move: R (rock), P (paper) or S (scissors)?")

# class RPS:
#     def __init__():

def get_computer_choice():
    computer_choice = random.choice(categories)
    print(computer_choice)
    return computer_choice

def get_user_choice():
    user_choice = input("What move will you play: (R) rock, (P) paper or (S) scissors? [R/P/S]?\t")
    user_choice = user_choice.upper()
    print(user_choice)
    if user_choice.upper() not in categories:
        print("Oops! That is not a recognised move. Type a letter to pick a move: R (rock), P (paper) or S (scissors)?")
    return user_choice

def get_winner(computer_choice, user_choice):
    print(computer_choice)
    print(user_choice)
    if computer_choice == user_choice:
        print(f"It's a tie! You both chose {computer_choice}.")
        winner = "It's a tie!"
    elif (computer_choice == "R" and user_choice == "P") or (computer_choice == "P" and user_choice == "S") or (computer_choice == "S" and user_choice == "R"):
        print(f"Congratulations! You won the game! Your {user_choice} beat {computer_choice}.")
        winner = "You won the game!"
    elif (computer_choice == "R" and user_choice == "S") or (computer_choice == "P" and user_choice == "R") or (computer_choice == "S" and user_choice == "P"):
        print(f"Oh no! You lost. Better luck next time! Your {user_choice} lost to {computer_choice}.")
        winner = "The computer won the game."
    else:
        print("I don't know what happened but none of the choices applied!")
        winner = "No winner."
    print(winner)
    return winner

def play():
    # get_computer_choice()
    # get_user_choice()
    get_winner(get_computer_choice(), get_user_choice())

play()
