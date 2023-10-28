import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nenter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
    if playerchoice not in ["1", "2", "3"]:
        print("you must enter 1 , 2  ,3")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("your chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python choise " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        print("🥳User win")
    elif player == 2 and computer == 1:
        print("🥳User win")
    elif player == 3 and computer == 2:
        print("🥳User win")

    elif player == computer:
        print("😒tie game my friend")
    else:
        print("🐍computer wins")
    print("\nPlay Again?")
    while True:
        playagain = input("\nPlay Again? \nY for yes or \nQ to quit \n")

        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n ")
        print("Better luck next time")
        sys.exit("Bye")


play_rps()
