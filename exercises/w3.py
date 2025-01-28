# 1. Check Nineteen and Five Occurrences

# Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.

lst = [1,19,19,5,5]
brojac_19 = 0
brojac_5=0
for broj in lst:
    if broj == 19:
        brojac_19+=1
    elif broj == 5:
        brojac_5 +=1
if brojac_19 == 2 and brojac_5 >=3:
    print("True")
else:
    print("False")
# if lst.count(19) == 2 and lst.count(5) >=3:
#     print("True")
# else:
#     print("False")