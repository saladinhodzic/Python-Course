# Classes

# creating class using class keyword

class User:
    def __init__(self,user_id):
        self.id=user_id
        self.followers=0
        self.following=0
    def follow(self,user):
        self.following+=1
        user.followers+=1

user1=User("001")
user2=User("002")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)