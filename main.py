import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(fun=player.up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 2) == 1:  # 1 in 2 chance per frame
        car_manager.new_blocks()
    car_manager.moving_block()
    if player.ycor()>290:
        player.reset()
        scoreboard.level()
        car_manager.speed_up_block()
    for turtle in car_manager.turtle_list:
        if turtle.distance(player) <25:
            scoreboard.write_game_over()
            game_is_on=False

screen.exitonclick()