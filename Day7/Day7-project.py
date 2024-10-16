# hangman
import random
import Day7_words
import Day7_art

logo=Day7_art.logo
art=Day7_art.stages
words=Day7_words.word_list

lives=6
random_word=random.choice(words)
blanks=''

print(logo)
print(random_word)

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
    