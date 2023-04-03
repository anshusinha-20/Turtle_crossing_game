"""imported Turtle class from turtle module"""
from turtle import Turtle

"""car forward distance"""
FORWARD = 20

"""created Car class"""
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)

    def move(self):
        self.forward(FORWARD)
