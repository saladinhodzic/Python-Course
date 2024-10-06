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