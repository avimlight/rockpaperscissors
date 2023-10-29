import sys
import random
from enum import Enum


def guess(name="PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_rps():
        nonlocal player_wins

        nonlocal name

        class RPS(Enum):
            ONE = 1
            TWO = 2
            THREE = 3

        playerchoice = input(
            f"\n{name},guess which number im thinking about {RPS(1).value},{RPS(2).value},{RPS(3).value}:\n\n"
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
            if player == computer:
                player_wins += 1
                return f" {name} you win"
            else:
                return f"sorry {name} better luck next time"

        winner = decide_winner(player, computer)
        print(winner)
        nonlocal game_count
        game_count += 1

        print(f"\nGame count  {game_count}")
        print(f"\n{name}'s wins { player_wins}")
        print(f"\n your winning percentage is :{player_wins/game_count:.2%}")

        print(f"\nPlay Again?,{name}")
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
            if __name__ == "__main__":
                sys.exit(f"Bye {name}")
            else:
                return  # this return is because it should run in my arcade file

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

    guess_my_number = guess(args.name)
    guess_my_number()
