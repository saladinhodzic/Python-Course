# Guessing number game
import random

print("Guess the number between 0 and 100")
random_num=random.randint(0,100)

difficulty=input("Choose the difficulty 'easy' or 'hard': ")

if difficulty=='easy':
    lives=10
else:
    lives=5

got_right_answer=False
    
while lives!=0 and got_right_answer==False:

    guess=int(input("Guess the number: "))

    if guess==random_num:
        print("Wow you got the right answer")
        got_right_answer=True
    elif guess<random_num:
        print("Too low")
        lives-=1
        print(f"You have {lives} remaining lives")
        
    elif guess > random_num:
        print("Too high")
        lives-=1
        print(f"You have {lives} remaining lives")
        