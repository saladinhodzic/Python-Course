bidders={}
print("Start bidding")

def check_bidders():
    user_name=input("Enter your name ")
    user_bid=int(input("Enter your bidding value $ "))
    bidders[user_name]=user_bid

check_bidders()

other_bidders=input("Are there other bidders? ")

while other_bidders=='yes':
    check_bidders()
    other_bidders=input("Are there other bidders? ")

print(bidders)