# Catching potential errors with try - expect block

try:
    age=int(input("Enter your age"))
except ValueError:
    print("Please enter a numerical value")
    age=int(input("Enter your age"))

print(age)