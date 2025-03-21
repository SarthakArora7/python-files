# import colorgram
#
# colors = colorgram.extract('painting.jpg', 30)
# # print(colors)
# color_list = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
# print(color_list)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

color_list = [(5, 13, 37), (38, 21, 16), (130, 89, 57), (201, 140, 118), (234, 210, 85), (187, 138, 162), (213, 86, 69),
              (79, 8, 20), (38, 137, 63), (194, 80, 100), (145, 85, 104), (31, 87, 29), (74, 107, 139), (220, 177, 212),
              (25, 203, 173), (126, 160, 180), (152, 138, 63), (13, 71, 25), (10, 61, 136), (115, 186, 157),
              (123, 12, 31), (86, 133, 174), (21, 208, 218), (230, 175, 166), (240, 208, 6), (133, 223, 206)]
tal = Turtle()


def new_position(j):
    new_pos = (0.00, 50.00 * j)
    tal.hideturtle()
    tal.penup()
    tal.goto(new_pos)
    tal.pendown()
    tal.showturtle()
    return


for j in range(10):
    if j > 0:
        new_position(j)
    for i in range(10):
        tal.color(random.choice(color_list))
        tal.shape("circle")
        tal.dot(20)
        tal.penup()
        tal.forward(50)
        tal.pendown()

screen = Screen()
screen.exitonclick()
