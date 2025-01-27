from colorgram import extract
import turtle as turtle_module
import random

# extracting hirst painting colors
colors = extract('hirstPainting.jpg', 37)
rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
real_rgb_colors = [rgb_color for rgb_color in rgb_colors[1:]]

#change colormode to 255 so that it can take rgp color
turtle_module.colormode(255)

tim = turtle_module.Turtle()

tim.penup()
tim.hideturtle()
tim.goto(-300,-250)
tim.speed("fast")


nb_row = 11
nb_dot_row = 11

for row in range(nb_row):
    for _ in range (nb_dot_row):
        tim.fd(50)
        tim.dot(20, random.choice(real_rgb_colors))

    tim.goto(-300, tim.ycor()+50)

#creating a screen instance and close it only on click
screen = turtle_module.Screen()
screen.exitonclick()