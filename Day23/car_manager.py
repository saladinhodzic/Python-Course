from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.cars=[]
        self.hideturtle()
    def spawn(self):
        for vehicle in range(1):
            vehicle = Turtle("square")
            vehicle.shapesize(1,2)
            vehicle.color(random.choice(COLORS))
            vehicle.penup()
            random_y = random.randint(-250,250)
            vehicle.goto(300,random_y)
            self.cars.append(vehicle)
    def move(self):
        for car in self.cars:
            car.goto(car.xcor()-(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level),car.ycor())
