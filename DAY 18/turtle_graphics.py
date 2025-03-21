import turtle
from turtle import Turtle, Screen
import random

tau = Turtle()
tau.shape("turtle")
turtle.colormode(255)


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# for i in range(15):
#     tau.forward(10)
#     tau.penup()
#     tau.forward(10)
#     tau.pendown()


#
#
# for i in range(3, 11):
#     angle = 360 / i
#     tau.color(change_color())
#     for j in range(i):
#         tau.forward(100)
#         tau.right(angle)


# directions = [0, 90, 180, 270]
#
# tau.pensize(10)
# tau.speed("fastest")
#
# for i in range(200):
#     tau.forward(30)
#     tau.setheading(random.choice(directions))
#     tau.color(change_color())

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tau.speed("fastest")
        tau.color(change_color())
        tau.circle(100)
        tau.setheading(tau.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()
