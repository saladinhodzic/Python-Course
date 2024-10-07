# Integers- Celi brojevi
print(123_345)

# Float- Decimalni brojevi
print(123.3)

# Boolean
print(True)

# Checking type of data values

print(type(123))
print(type('123'))
print(type(123.12))
print(type(True))

# Coding exercise

name_of_user=input("Enter name ")
length_of_name=len(name_of_user)


print("Number of letters in your name: " + str(length_of_name))

# When dividing in Python using / you will always get float number
# you can use // to get integer number
# // remove all decimals 

print(6/2)
print(6//2)

# Rounding numbers
# using round() method which takes two arguments, number, to how much decimals
bmi=78/180

print(round(bmi,2))

# f-string

score=1

print(f"Your score is {score}")

# Tip calculator

total_bill=float(input('How much is the the total bill? $'))
tip_percentage=float(input("How much tip you want to give? 10, 12, 15% "))

bill_tip=total_bill + total_bill/tip_percentage

costumers=int(input('How much people were at the table?'))

final_price=bill_tip/costumers


print(f"Each person should pay: {final_price}$")