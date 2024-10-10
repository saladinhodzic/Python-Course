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