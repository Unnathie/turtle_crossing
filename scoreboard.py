FONT = ("OCR A Extended", 20, "normal")
from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.level_up = 1
        self.level_no = Turtle()
        self.level_no.color("black")
        self.level_no.hideturtle()
        self.level_no.penup()
        self.level_no.goto(-220,260)
        self.level_no.write(arg=f"LEVEL : {self.level_up}", align="center", font=FONT)
    def write_game_over(self):
        self.game_over=Turtle()
        self.game_over.hideturtle()
        self.game_over.color("red")
        self.game_over.penup()
        self.game_over.write(arg="💀💀GAME OVER💀💀", align="center", font=("Snap ITC", 35, "normal"))
    def level(self):
        self.level_up+=1
        self.level_no.clear()
        self.level_no.write(arg=f"LEVEL : {self.level_up}", align="center", font=FONT)

