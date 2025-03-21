import turtle
from turtle import Turtle, Screen

tal = Turtle()


def right():
    tal.right(10)


def left():
    tal.left(10)


def forward():
    tal.forward(10)


def backward():
    tal.backward(10)


def clear():
    tal.clear()
    tal.penup()
    tal.home()
    tal.pendown()


turtle.onkeypress(key="d", fun=right)
turtle.onkeypress(key="a", fun=left)
turtle.onkeypress(key="w", fun=forward)
turtle.onkeypress(key="s", fun=backward)
turtle.onkeypress(key="c", fun=clear)

screen = Screen()
screen.listen()
screen.exitonclick()
