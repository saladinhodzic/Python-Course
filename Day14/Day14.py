# Higher Lower Game
from Day14_data import data
import random

score = 0

a=random.choice(data)
b=random.choice(data)
print(a['name'])

print(b['name'])

a_follower_count=a["follower_count"]
b_follower_count=b["follower_count"]


lower_or_higher=input("Which of these two are more popular 'A' or 'B': ")

if lower_or_higher=='A':
    if a_follower_count>b_follower_count:
        print("Bingo")
