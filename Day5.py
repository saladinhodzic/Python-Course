# for loop

fruits=['apple','pear','cherry']

for fruit in fruits:
    print(fruit)

student_scores = [180, 124, 165, 173, 189, 169, 146]

# print(sum(student_scores)) sum method for accumulating the result
sum=0
for score in student_scores:
    sum+=score

print(sum)

# finding largest number in list

# print(max(student_scores)) max method for finding largest number in list

number=0

for score in student_scores:
    if score>number:
        number=score

print(number)

# range function - first argument is the number which we start from second argument is where we want to stop
#  third argument is the increment we can put some number for exp 2 and its gonna skip two steps


for number in range(1,10):
    print(number)

zbir=0

for number in range(1,101,1):
    zbir+=number


print(zbir)