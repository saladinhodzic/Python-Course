# Making decorator function

def decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper
class User():
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False
user = User("saki")
user.is_logged_in = True
@decorator
def create_post(user):
    print(f"{user.name} created the post")
create_post(user)
# def decorator(function):
#     def wrapper():
#         time.sleep(2)
#         function()
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello")

# say_hello()