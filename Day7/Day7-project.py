# hangman
import random
from Day7_art import stages,logo
from Day7_words import word_list


lives=6
random_word=random.choice(word_list)
blanks=''
game_over=False
correct_letters=[]

print(logo)
print(random_word)

for letter in range(len(random_word)):
    blanks+="_"

print(blanks)

while not game_over:
    display=""
    user_guess=input("Enter letter lowercase: ").lower()
        
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
        print(stages[lives])
        if lives==0:
            game_over=True
    
    if "_" not in display :
            game_over=True
    print(lives)
    