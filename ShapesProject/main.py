from turtle import Turtle, Screen
import random

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(0,100)
tim.pendown()
def draw_shap(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

shape_color = ["midnight blue", "medium aquamarine", "sea green", "maroon", "dark magenta", "magenta", "medium violet red", "firebrick", "dark slate blue", "yellow", "pale green"]

for shape_side_num in range(3, 11):
    tim.color(random.choice(shape_color))
    draw_shap(shape_side_num)
screen = Screen()
screen.exitonclick()