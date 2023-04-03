"""imported Turtle class from the turtle module"""
from turtle import Turtle

"""created player class"""
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
