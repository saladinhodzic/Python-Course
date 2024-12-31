# 6. List and Tuple Generator

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# numbers = input("Enter sequence of numbers comma separated: ").split(", ")
# torka = tuple(numbers)
# print(numbers,torka)

'''7. File Extension Extractor

Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''

# file_name = input("Enter file name: ").split(".")
# print(file_name[1])

'''10. Number Expansion Calculator

Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''

# n = int(input("Enter number for expansion: "))

# acc= n + (n*10+n) + (n*100 + n*10 + n)

# print(acc)

'''1. Check Nineteen and Five Occurrences

Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True'''

# def check_19_and_5(list):
#     acc1=0
#     acc2=0
#     for broj in list:
#         if broj == 19:
#             acc1+=1
#         elif broj == 5:
#             acc2+=1
#     if acc1 == 2:
#         if acc2 >=3:
#             return True
#     else:
#         return False
# lista = map(int,input("Enter a list of nubers: ").split(" "))
# print(check_19_and_5(lista))

'''2. Fifth Element and List Length Check

Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True'''

numbers = list(map(int,input("Enter a list of integers: ").split(" ")))
def length_and_fifth(lista):
    if len(lista)==8 and lista.count(lista[4]) == 3:
        return True
    return False
print(length_and_fifth(numbers))