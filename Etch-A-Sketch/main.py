from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.title("Etch-A-Sketch")
screen.listen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_right():
    tim.right(15)
def turn_left():
    tim.left(15)
def reset_turlte():
    tim.reset()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=reset_turlte)

screen.exitonclick()


