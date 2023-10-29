import sys
from rps8 import rps
from guessmynumbermodified import guess


def play_game(name="PlayerOne"):
    wc = False
    while True:
        if wc == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(
            '\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade\n\n'
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)
        wc = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    unini = play_game(args.name)
    unini()
