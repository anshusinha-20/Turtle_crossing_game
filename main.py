"""imported Screen class from the turtle module"""
from turtle import Screen

"""created screen object"""
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing game")
screen.bgcolor("white")

"""screen will exit on click"""
screen.exitonclick()
