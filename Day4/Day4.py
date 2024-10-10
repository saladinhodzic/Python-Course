# random module
import random
import my_module
random_int=random.randint(1,10)


print(random_int)

print(my_module.my_number)

random_number_0_to_1=random.random()

print(random_number_0_to_1)

# tails or head game

if random_number_0_to_1<0.5:
    print('Tails')
else:
    print("Head")

# list

fruits=['pear','apple','banana']

fruits.append('cherry')

print(fruits)

# friends

friends=["Charlie","Emanuel","Sara",'Me']

# print(friends[random.randint(0,3)])

# 2nd way
print(random.choice(friends))