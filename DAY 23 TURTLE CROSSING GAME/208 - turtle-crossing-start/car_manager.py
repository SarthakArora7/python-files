from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            self.all_cars.append(car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.moving_speed)

    def increment_speed(self):
        self.moving_speed += MOVE_INCREMENT

