# Making decorator function
import time
def decorator(function):
    def wrapper():
        time.sleep(2)
        function()
    return wrapper
@decorator
def say_hello():
    print("Hello")

say_hello()