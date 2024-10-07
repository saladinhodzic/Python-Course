# introducing conditional statements

height=120

if height>=120:
    print("You are okay")
else:
    print("Grow taller")    

#check if number is even or odd

number=int(input('Enter number'))

if number%2==0:
    print("Number is even")
    age=int(input('Enter your age'))
    
    if age<=12:
        print('7$')
    elif age<18:
        print('10$')
    else:
        print("12$")    


else:
    print("Number is odd")    
