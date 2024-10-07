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
