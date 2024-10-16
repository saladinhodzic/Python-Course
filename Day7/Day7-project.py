# hangman
import random

words=['cat','cookie','sticks','paper','scissors','player','women','box']
lives=6

random_word=random.choice(words)
print(random_word)
blanks=''
for letter in range(len(random_word)):
    blanks+="_"
print(blanks)

game_over=False
correct_letters=[]
while not game_over:

    display=""
    user_guess=input("Enter letter lowercase: ")
    for letter in random_word:
        if user_guess == letter:
            display+=letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+='_'
            
            
    print(display)

    if user_guess not in random_word:
        lives-=1
        if lives==0:
            game_over=True
    
    if "_" not in display :
            game_over=True
    print(lives)
    