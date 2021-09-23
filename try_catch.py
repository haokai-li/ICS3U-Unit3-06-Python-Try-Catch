#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program guess a number between 0 - 9 (random)

import random


def main():
    # This function guess a number between 0 - 9 (random)
    answer = random.randint(0, 9)

    # input
    guess_string = input("Enter a number between 0 - 9: ")
    print("")

    # process
    try:
        guess_number = int(guess_string)
        print("Incoorect, the number was {}.".format(guess_number))
        if guess_number == answer:
            # output
            print("You guessed correctly!")
        else:
            # output
            print("You guessed wrong!")
            print("Answer: {}".format(answer))
    except Exception:
        print("{} is not an integer.".format(guess_string))
    finally:
        print("Thanks for playing.")

    print("\nDone")


if __name__ == "__main__":
    main()
