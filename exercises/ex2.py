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

# nums = [1,2,3,4,5,6,7]

# replace = [-1 if num % 2 != 0 else num for num in nums]

# print(replace)

'''Exercise 6:

Convert a list of integers to a list of booleans where all non-zero values become True.

'''

# nums = [1,2,3,0,0,2,5]

# convert = [bool(num) for num in nums]

# print(convert)

'''Exercise 7:

Replace all even numbers in a list with their negative.

'''

# nums = [1,2,3,4,5,6]

# replace = [num * -1 if num % 2 == 0 else num for num in nums]

# print(replace)

'''Exercise 8:

Create a 3x3 list of lists with random values and normalize it.

'''
# import random

# matrix = [[random.randint(1,100) for _ in range(3)] for _ in range(3)]

# flatten_matrix = [num for row in matrix for num in row]

# min = min(flatten_matrix)
# max = max(flatten_matrix)

# normalized_matrix = [[round((value - min ) / (max - min),2) for value in row ] for row in matrix]

# print(normalized_matrix)


'''Exercise 9:

Calculate the sum of the diagonal elements of a 3x3 matrix (list of lists).

'''

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# diagonal_elements = []

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i==j:
#             diagonal_elements.append(matrix[i][j])

# print(sum(diagonal_elements))

'''
Exercise 10:

Find the indices of non-zero elements in a list.

'''

# nums = [1,0,2,0,3,4]

# non_zero_indices = [i for i in range(len(nums)) if nums[i] != 0]

# print(non_zero_indices)

'''
Exercise 11:

Reverse a list.

'''

# arr = [1,2,3,4,5,6]

# # reverse = [arr[i] for i in range(len(arr)-1,-1,-1)]
# reverse = arr[::-1]

# print(reverse)

'''Exercise 12:

Create a 3x3 identity matrix as a list of lists.

'''

# matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

# print(matrix)

'''Exercise 13:

Reshape a 1D list to a 2D list with 2 rows.

'''

# one_dimension = [1,2,3,4,5]
# two_dimension = [one_dimension[:len(one_dimension)//2] , one_dimension[len(one_dimension)//2:]]
# print(two_dimension)

'''
Exercise 14:

Stack two lists vertically.

'''

# first = [1,2,3]
# second = [4,5,6]
# stack = [first,second]
# print(stack)

'''Exercise 15:

Get the common items between two lists.

'''

# first = [1,2,3,4,5]
# second = [4,5,2,6,7]
# # common_items = [first[i] for i in range(len(first)) for j in range(len(second))  if first[i] == second[j] ]
# common_items = list(set(first) & set(second))

# print(common_items)

'''Exercise 16:

Create a 5x5 list of lists with row values ranging from 0 to 4.

'''

# matrix = [[value for value in range(5)] for _ in range(5)]
# print(matrix)

'''Exercise 17:

Find the index of the maximum value in a list.
'''

# nums = [1,2,3,4,5,6,7]

# max = max(nums)

# print(nums.index(max))

'''Exercise 18:

Normalize the values in a list between 0 and 1.

'''

# nums = [1,2,3,4,5,6,7]

# min = min(nums)
# max = max(nums)

# normalized_list = [round((value - min) / (max - min),2) for value in nums]

# print(normalized_list)

'''
Exercise 19:

Calculate the dot product of two lists.

'''

# first_list = [1,2,3,4,5]
# second_list = [6,7,8,9,10]    
# # sum=0
# # for i in range(len(first_list)):
# #     sum+=first_list[i] * second_list[i]
# sum = sum(x * y for x, y in zip(first_list,second_list))
# print(sum)

'''Exercise 20:

Count the number of elements in a list within a specific range.
'''

# nums = [1,2,3,4,5,6,7]

# count = sum(5 <= num <=10 for num in nums)

# print(count)

'''Exercise 21:

Find the mean of each row in a 2D list.

'''

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# for row in matrix:
#     suma = 0
#     for broj in row:
#         suma += broj
#     print(suma / len(row))

# import random 

# matrix = [[random.random() for _ in range(3)] for _ in range(3)]

# means = [sum(row) / len(row) for row in matrix]
# print(matrix)
# print(means)

'''Exercise 22:

Create a random 4x4 list of lists and extract the diagonal elements.

'''
# import random
# matrix = [[random.randint(0,10) for _ in range(4)]for _ in range(4)]

# diagonal_elements = [matrix[i][i] for i in range(len(matrix)) ]

# print(diagonal_elements)

'''Exercise 23:

Count the number of occurrences of a specific value in a list.'''

# nums = [1,1,2,2,3,4,5,5,5]

# print(nums.count(5))

'''
Exercise 24:

Replace all values in a list with the mean of the list.

'''

# nums = [1,2,3,4,5,6,4,2,9]

# mean = [sum(nums)/len(nums) for _ in range(len(nums))]
# print(mean)

'''
Exercise 25:

Find the indices of the maximum and minimum values in a list.
'''

# lst = [5, 2, 8, 1, 7]

# max_index = lst.index(max(lst))
# min_index = lst.index(min(lst))

'''
Exercise 26:

Create a 2D list with 1 on the border and 0 inside.
'''

# matrix = [[1 if i == 0 or i == 3  or j == 0 or j == 3 else 0 for j in range(4)]for i in range(4)]
 
# print(matrix)

'''
Exercise 27:

Find the unique values and their counts in a list.
'''

# lst = [1, 2, 3, 2, 4, 1, 5, 4, 6]

# remove_duplicates = list(set(lst))
# find_counts = {broj:lst.count(broj) for broj in remove_duplicates}

# print(remove_duplicates)
# print(find_counts)

'''Exercise 28:

Create a 3x3 list of lists with values ranging from 0 to 8.
'''
# matrix = [[i + j * 3 for i in range(3)]for j in range(3)]

# print(matrix)

'''
Exercise 29:

Calculate the exponential of all elements in a list.
'''
# import math
# lst = [1, 2, 3, 4, 5]

# exponents = [math.exp(broj) for broj in lst]
# print(exponents)

'''
Exercise 30:

Swap two rows in a 2D list.
'''

# import random

# matrix = [[random.randint(0,5) for _ in range(3)]for _ in range(2)]

# print(matrix)

# swap = [matrix[i] for i in range(1,-1,-1)]
# print(swap)


'''
Exercise 31:

Create a random 3x3 list of lists and replace all values greater than 0.5 with 1 and all others with 0.
'''

# import random

# matrix = [[random.random() for _ in range(3)] for _ in range(3)]

# swap = [[1 if broj > 0.5 else 0 for broj in row]for row in matrix]

# print(matrix)
# print(swap)

'''Exercise 32:

Find the indices of the top N maximum values in a list.
'''

lst = [10, 5, 8, 20, 15]
n = 3

indices = sorted(range(len(lst)), key= lambda i:lst[i], reverse=True)[:n]
print(indices)