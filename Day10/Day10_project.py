# calculator

def add(n1,n2):
    return n1+ n2
def sub(n1,n2):
    return n1- n2
def mult(n1,n2):
    return n1* n2
def div(n1,n2):
    return n1/ n2

operators={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}

print(operators["*"](4,8))

first_num=int(input('Enter first number: '))
operator=input("Enter the operator: ")
second_num=int(input('Enter second number: '))

result=operators[operator](first_num,second_num)
print(result)

extend_result=input("Do you want to continue working with this result or no?\ntype y or n")



while extend_result=='y':
    operator=input("Enter the operator: ")
    second_num=int(input('Enter second number: '))
    result=operators[operator](result,second_num)
    print(result)
    extend_result=input("Do you want to continue working with this result or no?\ntype y or n ")