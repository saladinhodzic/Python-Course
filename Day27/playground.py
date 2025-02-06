def add(*args):
    result = 0
    for num in args:
        result+=num
    return result
print(add(1,2,3,4,5))