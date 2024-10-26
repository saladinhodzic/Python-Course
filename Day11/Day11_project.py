# Blackjack
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards=[]
my_cards=[]
dealer_score=0
my_score=0

wanna_play=input("Do you want to play Blackjack y or n? ")

def check_end(my_score,dealer_score):
    if my_score==21 or dealer_score==21:
        print("Blackjack")

def draw_first_cards(dealer_score,my_score):
    for card in range(2):
        my_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_score+=dealer_cards[card]
        my_score+=my_cards[card]
    print(f"Your cards are {my_cards[0]} and {my_cards[1]}")
    print(my_score)
    print(f"Dealers cards are {dealer_cards[0]} _")
    
    check_end(my_score=my_score,dealer_score=dealer_score)

if wanna_play == 'y':
    draw_first_cards(dealer_score,my_score)