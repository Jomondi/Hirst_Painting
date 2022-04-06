import turtle
from turtle import Turtle, Screen
import random
from color_extractor import color_list

timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)


def pen(x, y):
    timmy.penup()
    timmy.setposition(x, y)


pen(-250, -240)


def draw():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


for vals in range(10):
    draw()
    pen(-250, timmy.ycor() + 50)

timmy.hideturtle()
screen = Screen()
screen.exitonclick()
