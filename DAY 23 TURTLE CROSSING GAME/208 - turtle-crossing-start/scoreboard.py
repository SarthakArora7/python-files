from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y=250)
        self.write(f"Level: {self.level}", align="Left", font=("Arial", 24, "normal"))

    def game_over(self):
        game = Turtle()
        game.write("Game Over", align="Center", font=("Arial", 24, "normal"))

    def next_level(self):
        self.level += 1
        self.display_level()

