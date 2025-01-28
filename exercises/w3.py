# 1. Check Nineteen and Five Occurrences

# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

# lst = [1,19,19,5,5]
# brojac_19 = 0
# brojac_5=0
# for broj in lst:
#     if broj == 19:
#         brojac_19+=1
#     elif broj == 5:
#         brojac_5 +=1
# if brojac_19 == 2 and brojac_5 >=3:
#     print("True")
# else:
#     print("False")
# if lst.count(19) == 2 and lst.count(5) >=3:
#     print("True")
# else:
#     print("False")

# 2. Fifth Element and List Length Check

# Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

# lst = [1,2,3,4,5,5,5,6]
# if len(lst) == 8 and lst.count(lst[4]) == 3:
#     print("True")
# else:
#     print("False")

# Napisi program koji prihvata listu floatova i gleda da li je sredisnji element liste aritmeticka sredina liste
length = int(input("Unesite duzinu liste: "))
lst = [float(input("Unesite element liste")) for _ in range(length)]

sredisnji_element = length//2
arit_sredina = sum(broj for broj in lst) / length
if lst[sredisnji_element] == arit_sredina:
    print("True")
else:
    print("False")