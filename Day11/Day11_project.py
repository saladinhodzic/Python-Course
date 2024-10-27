# Blackjack
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards=[]
my_cards=[]
dealer_score=0
my_score=0

wanna_play=input("Do you want to play Blackjack y or n? ")

def draw_again_card(user_or_dealer,my_score,dealer_score):
    if user_or_dealer=='user':
        check_if_ace=random.choice(cards)
        if check_if_ace == 11 and my_score+11>21:
            my_cards.append(1)
            my_score+=my_cards[len(my_cards)-1]
        elif check_if_ace == 11:
            my_cards.append(11)
            my_score+=my_cards[len(my_cards)-1]
        else:
            my_cards.append(check_if_ace)
            my_score+=my_cards[len(my_cards)-1]
        print(my_cards)
        print(my_score)
        check_end(my_score,dealer_score)
    else:
            dealer_cards.append(random.choice(cards))
            dealer_score+=dealer_cards[len(dealer_cards)-1]
            print(dealer_cards)
            print(dealer_score)
            check_end(my_score,dealer_score)
        
def check_end(my_score,dealer_score):
    if my_score==21 or dealer_score==21:
        if my_score==21:
            print("You win Blackjack")
        else:
            print("You lost")
        return
    elif my_score>21 or dealer_score>21:
        if my_score>21:
            print("You lost your score is over 21")
            return
        else:
            print("You win dealers score is over 21")
            return
        
    elif my_score>=16 and dealer_score>=16:
        wanna_draw_another_card=input("Do you wanna draw another card or not? ")
        if wanna_draw_another_card=='y' :
                draw_again_card(user_or_dealer='user',my_score=my_score,dealer_score=dealer_score)
        else:
                draw_again_card(user_or_dealer='dealer',my_score=my_score,dealer_score=dealer_score) 
        if my_score> dealer_score:
            print(f"You win your score is {my_score} and dealer score is {dealer_score}")
            return
        else:
            print(f"You lost your score is {my_score} and dealers score is {dealer_score}")
            return
    else: 
         wanna_draw_another_card=input("Do you wanna draw another card or not? ")
         if wanna_draw_another_card=='y' :
             draw_again_card(user_or_dealer='user',my_score=my_score,dealer_score=dealer_score)
         else:
             draw_again_card(user_or_dealer='dealer',my_score=my_score,dealer_score=dealer_score) 

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