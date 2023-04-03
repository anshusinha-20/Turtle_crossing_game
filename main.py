"""imported Screen class from the turtle module"""
from turtle import Screen

"""imported time module"""
import time

"""imported Player class from the player module"""
from player import Player

"""created screen object"""
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.bgcolor("white")
screen.tracer(0)

"""created player object"""
player = Player()

"""variable to hold the game's running condition"""
isGameOn = True

"""until the game is on, the loop will run"""
while isGameOn:
    screen.update()
    time.sleep(0.08)

"""screen will exit on click"""
screen.exitonclick()
