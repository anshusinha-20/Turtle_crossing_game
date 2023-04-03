"""imported Screen class from the turtle module"""
import time
from turtle import Screen

"""created screen object"""
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.bgcolor("white")
screen.tracer(0)

"""variable to hold the game's running condition"""
isGameOn = True

"""until the game is on, the loop will run"""
while isGameOn:
    screen.update()
    time.sleep(0.08)

"""screen will exit on click"""
screen.exitonclick()
