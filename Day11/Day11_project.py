# Blackjack
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards=[]
my_cards=[]
dealer_score=0
my_score=0

wanna_play=input("Do you want to play Blackjack y or n? ")

def draw_cards(dealer_score,my_score):
    for card in range(2):
        my_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_score+=dealer_cards[card]
        my_score+=my_cards[card]
    print(my_cards)
    print(my_score)
    print(dealer_cards[0])
    print(dealer_score)
if wanna_play == 'y':
    draw_cards(dealer_score,my_score)