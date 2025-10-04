# Project Task 1

# Number Guessing Game

# NECESSARY IMPORTS
import random
import streamlit as st

def intro():
    return ("Welcome to the Number Guessing Game")


def set_difficulty():
    global end, start

    print("""Choose the difficulty from below:
          1. Easy
          2. Medium
          3. Hard""")
    choice = input("Enter your difficulty level: ")
    if choice in ['1', 'Easy', '1. Easy']:
        start = 1
        end = 3
        return "Easy"   
    elif choice == '2':
        start = 1
        end = 10
        return "Medium"
    elif choice == '3':
        start = 1
        end = 50
        return "Hard"
    else:
        print("Wrong Choice, Try Again")
        set_difficulty()


def game():
    '''Number Guessing Game: A classic game where the computer thinks of a number and the user has to guess it.'''

    system_choice = random.randint(start, end)
    count = 1
    while True and count < 10:
        user_choice = int(input("Guess the number : "))
        if user_choice == system_choice:
            print("Well Done, Hurray!!!")
            return f"Guessed in {count} go"
        else:
            count += 1
            if user_choice < system_choice:
                print("Wrong guess, Try Again!\nTry something greater")
            else:
                print("Wrong guess, Try Again!\nTry something smaller")
            continue
    else:
        return f"Limit Exceeded - Failed\nThe number was {system_choice}"


def main():
    print(intro())
    set_difficulty()
    print(game())


if __name__ == "__main__":
    main()
