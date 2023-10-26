import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("you must enter 1 , 2  ,3")

computerchoice = random.choice("123")
computer = int(computerchoice)
print("")
print("your chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python choise " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")
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
