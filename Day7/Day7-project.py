# hangman
import random

words=['cat','cookie','sticks','paper','scissors','player','women','box']

lives=6


def starting_game():
    random_word=random.choice(words)
    user_guess=input("Enter letter lowercase: ")
    for letter in random_word:
        if user_guess == letter:
            print("You got one")
        else:
            print("You messed up")

starting_game()