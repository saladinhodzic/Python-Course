# introducing conditional statements

height=120

if height>=120:
    print("You are okay")
else:
    print("Grow taller")    

#check if number is even or odd

number=int(input('Enter number'))
bill=0

if number%2==0:
    print("Number is even")
    age=int(input('Enter your age'))
    
    if age<=12:
        bill=7
        print('7$')
    elif age<18:
        bill=10
        print('10$')
    else:
        bill=12
        print("12$")    

    photo=input('Photo or not')

    if photo=='yes':
        bill+=3

    print(f"Total bill is {bill}")
else:
    print("Number is odd")    

# Pizza exercise

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=='S':
    bill+=15
    
elif size == "M":
    bill+=20
    
else:
    bill+=25
    

if pepperoni == "Y":
    if size=='S':
        bill+=2
    else:
        bill += 3

if extra_cheese=='Y':
    bill+=1

print(bill)

# Island Treasure Game

direction=input("You arrive at some place, do you want go left or right?")

if direction != 'right':
    wait_or_not=input("You see lake and island, do you want to wait for boat or swim accross")

    if wait_or_not == 'wait':
        house=input("You arrived on island and you see three houses, red, yellow and blue. Which one you choose?")

        if house != 'red' and house != 'blue':
            print("You win!")

        else:
            print("You lose.")

    else:
        print('Game over')

else:
    print("Game over")