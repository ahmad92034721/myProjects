import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()
tim.speed("fastest")

def draw_spirograph(gap_size):
    for _ in range(360 // gap_size):
        tim.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(3   )

screen = Screen()
screen.exitonclick()