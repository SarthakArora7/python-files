import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_car()

    # Detection of collision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Restarting when reaching top
    if player.ycor() > 280:
        player.restart()
        carmanager.increment_speed()
        scoreboard.next_level()

screen.exitonclick()

