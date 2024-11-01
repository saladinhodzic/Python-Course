# Higher Lower Game
from Day14_data import data
import random

score = 0

is_playing=True

while is_playing==True:

    a=random.choice(data)
    b=random.choice(data)


    a_follower_count=a["follower_count"]
    b_follower_count=b["follower_count"]

    print(a['name'])
    print(b['name'])

    lower_or_higher=input("Which of these two are more popular 'A' or 'B': ")

    if lower_or_higher=='A':
        if a_follower_count>b_follower_count:
            score+=1
            print("Bingo")
            print(f"Your score is {score}")
        else:
            print(f'You lost! Your score is {score}')
            is_playing=False
    if lower_or_higher=='B':
        if  b_follower_count>a_follower_count:
            score+=1
            print("Bingo")
            print(f"Your score is {score}")
        else:
            print(f'You lost! Your score is {score}')
            is_playing=False