# hangman
import random

words=['cat','cookie','sticks','paper','scissors','player','women','box']

lives=6

def guess():
   input("Enter letter lowercase")

def starting_game():
    random_word=random.choice(words)
    for letter in random_word:
        user_guess= guess()
        print(f"length is {len(random_word)}")
        if user_guess == letter:
            print("You got one")
        else:
            print("You messed up")

starting_game()