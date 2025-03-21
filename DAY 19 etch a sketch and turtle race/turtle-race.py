from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
turtles = []

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# ben = Turtle(shape="turtle")
# bat = Turtle(shape="turtle")
# cas = Turtle(shape="turtle")
# can = Turtle(shape="turtle")
# turtle_list = [tim, tom, bat, ben, can, cas]
is_race_on = True
if user_bet:
    while is_race_on:
        start_point_y = -150
        for turtle_index in range(0, 6):
            tim = Turtle(shape="turtle")
            tim.penup()
            tim.color(colors.pop())
            tim.goto(x=-230, y=start_point_y)
            start_point_y += 50
            turtles.append(tim)


print(turtles)
screen.exitonclick()

