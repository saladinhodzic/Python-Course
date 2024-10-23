bidders={}
highest_bidder=''
highest_value=0
print("Start bidding")

def check_bidders():
    user_name=input("Enter your name ")
    user_bid=int(input("Enter your bidding value $ "))
    bidders[user_name]=user_bid

check_bidders()

other_bidders=input("Are there other bidders? ")

while other_bidders=='yes':
    print('\n'*100)
    check_bidders()
    other_bidders=input("Are there other bidders? ")

for key in bidders:
    if bidders[key]>highest_value:
        highest_value=bidders[key]
        highest_bidder=key
        
print("The highest bidder is {} with {} $.".format(highest_bidder,highest_value))