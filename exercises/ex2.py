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

# numbers = list(map(int,input("Enter a list of integers: ").split(" ")))
# def length_and_fifth(lista):
#     if len(lista)==8 and lista.count(lista[4]) == 3:
#         return True
#     return False
# print(length_and_fifth(numbers))

'''3. Stone Piles Distribution

We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
Input: 2
Output:
[2, 4'''

# n_stones = int(input("Enter n of stone piles: "))
# n_piles = [n_stones]
# for stone in range(1,n_stones):
#     n_piles.append(n_piles[stone - 1] + 2)
# print(n_piles)

'''7. Sum of First i Equals i

Write a  Python program to check a given list of integers where the sum of the first i integers is i.'''

# def sum_of_i(list):
#     sum = 0
#     brojac = 1
#     for broj in list:
#         sum+=broj
#         if sum == brojac:
#             brojac+=1
#         else:
#             return False
#     return True
# print(sum_of_i([1, 1, 1, 1, 1, 1]))

'''8. Split String into Words and Separators

Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
Input: W3resource Python, Exercises.
Output:
[['W3resource', 'Python', 'Exercises.'], [' ', ', ']]'''
# def split(input):
#     words = []
#     sep = []
#     separators = ', -'
#     word = ''
#     for letter in input:
#         if letter not in separators:
#             word += letter
#         else:
#             if word != '':
#                 words.append(word)
#                 word= ''
#             sep.append(letter)
#     words.append(word)
#     print(words,sep)
# split("Danas je, lep dan.")

'''9. Four Distinct Values Non-Consecutive

Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
Input:
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
Output:
True'''

# def check(list):
#     for i in range(3,len(list)):
#         for j in range(i-1,i-4,-1):
#             if list[i] !=list[j]:
#                 pass
#             else:
#                 return False
#     return True

# print(check([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]))
# print(check([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]))

'''10. Split Matched Parentheses Groups

Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']'''

# def parentheses(input):
#     arr = []
#     match = ''
#     brojac1 = 0
#     brojac2 = 0
#     for symbol in input:
#         if symbol == ' ':
#             continue
#         match+=symbol
#         if symbol == '(':
#             brojac1+=1
#         else:
#             brojac2+=1
#         if brojac1 == brojac2 and brojac1 != 0:
#             arr.append(match)
#             match = ''
#             brojac1 = 0
#             brojac2 = 0
#     print(arr)
# parentheses('( ()) ((()()())) (()) ()')

'''12. Check Palindromes in List

Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]'''

# def check_palindroms(list):
#     is_palindrome = []
    
#     for word in list:
#         if word == word[::-1]:
#             is_palindrome.append(True)
#         else:
#             is_palindrome.append(False)
#     print(list)
#     print(is_palindrome)
# check_palindroms(['palindrome', 'madamimadam', '', 'foo', 'eyes'])

'''Exercise 1:

Create a list with values ranging from 0 to 9.

'''

# lista = list(range(10))
# print(lista)

'''Exercise 2:

Convert a list of integers to a list of strings.

'''

# lista_int = [1,2,3,4,5]

# lista_str = list(map(str,lista_int))

# print(lista_str)

'''Exercise 3:

Multiply all elements in a list by 2.

'''

# nums = [2,4,6,3,4]

# multiply = [elem * 2 for elem in nums]

# print(multiply)

'''Exercise 4:

Extract all odd numbers from a list of integers.

'''

# nums = [1,2,3,4,5]

# odd_nums = [elem for elem in nums if elem % 2 != 0]

# print(odd_nums)

'''Exercise 5:

Replace all odd numbers in a list with -1.

'''

nums = [1,2,3,4,5,6,7]

replace = [-1 if num % 2 != 0 else num for num in nums]

print(replace)