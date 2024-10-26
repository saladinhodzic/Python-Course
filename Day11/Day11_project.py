# Blackjack
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards=[]
my_cards=[]

wanna_play=input("Do you want to play Blackjack y or n? ")

def draw_cards():
    for card in range(2):
        my_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print(my_cards)
    print(dealer_cards[0])

if wanna_play == 'y':
    draw_cards()