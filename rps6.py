import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tiecount = 0

    def play_rps():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nenter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n"
        )
        if playerchoice not in ["1", "2", "3"]:
            print("you must enter 1 , 2  ,3")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\nyour chose {str(RPS(player)).replace('RPS.', '')}  ")
        print(f"\nPython choise   {str(RPS(computer)).replace('RPS.', '')}  .")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tiecount
            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳User win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳User win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳User win"

            elif player == computer:
                tiecount += 1
                return "😒tie game my friend"
            else:
                computer_wins += 1
                return "🐍computer wins"

        winner = decide_winner(player, computer)
        print(winner)
        nonlocal game_count
        game_count += 1

        print(f"\nGame count  {str(game_count)}")
        print(f"\nplayer wins { str(player_wins)}")
        print(f"\ncomputer wins { str(computer_wins)}")
        print(f"\ntie match is { str(tiecount)}")
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

    return play_rps


rock_paper_scissors = rps()
if __name__ == "__main__":
    rock_paper_scissors()
