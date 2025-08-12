from turtle import Turtle
import random

COLORS = [
    "red", "orange", "yellow", "green", "blue", "purple",
    "dark blue", "magenta", "maroon", "dark green", "navy",
    "indigo", "dark red", "teal", "midnight blue", "saddle brown",
    "slate gray", "dark slate gray", "firebrick"
]



class CarManager:
    def __init__(self):
        self.turtle_list = []
        self.new_blocks()
        self.speed=5

    def new_blocks(self):
        lane_y = random.randrange(-250, 250,40)
        # Check if lane already has a car too close to spawn area
        for car in self.turtle_list:
            if car.ycor() == lane_y and car.xcor() > 200:
                return  # Skip spawning this frame

        new_turtle = Turtle(shape="square")
        new_turtle.shapesize(stretch_len=2, stretch_wid=1)
        new_turtle.penup()
        new_turtle.color(random.choice(COLORS))
        new_turtle.goto(305, lane_y)
        self.turtle_list.append(new_turtle)

    def moving_block(self):
        for new in self.turtle_list:
            new.back(self.speed)
    def speed_up_block(self):
        self.speed+=5

