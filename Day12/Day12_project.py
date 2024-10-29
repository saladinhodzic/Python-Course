# Guessing number game
import random

print("Guess the number between 0 and 100")
random_num=random.randint(0,100)

difficulty=input("Choose the difficulty 'easy' or 'hard': ")

if difficulty=='easy':
    lives=10
else:
    lives=5

guess=input("Guess the number: ")