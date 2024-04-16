import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    tiecount = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins
        nonlocal tiecount
        nonlocal name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\{name},please enter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n"
        )
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name},please enter 1 , 2  ,3")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name},you chose {str(RPS(player)).replace('RPS.', '')}  ")
        print(f"\nPython choise   {str(RPS(computer)).replace('RPS.', '')}  .")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal tiecount
            if player == 1 and computer == 3:
                player_wins += 1
                return "🥳{name} win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🥳{name} win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🥳{name} win"

            elif player == computer:
                tiecount += 1
                return "😒tie game my friend"
            else:
                computer_wins += 1
                return f"🐍 computer wins\nSorry ,{name}...🥲"

        winner = decide_winner(player, computer)
        print(winner)
        nonlocal game_count
        game_count += 1

        print(f"\nGame count  {game_count}")
        print(f"\n{name}'s wins { player_wins}")
        print(f"\ncomputer wins { computer_wins}")
        print(f"\ntie match is { tiecount}")
        print("\nPlay Again?,{name}")
        while True:
            playagain = input(f"\n{name}Play Again? \nY for yes or \nQ to quit \n")

            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n ")
            print("Better luck next time")
            sys.exit(f"Bye {name}")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="provides a personalized game person")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="the name of the person palying the game ",
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
#this is the 7th process    
    
