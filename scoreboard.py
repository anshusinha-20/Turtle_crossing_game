"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""constants"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

"""created Scoreboard class"""
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
