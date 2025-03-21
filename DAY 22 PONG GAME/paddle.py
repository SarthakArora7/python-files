from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        y_new = self.ycor() + 20
        self.goto(self.xcor(), y_new)

    def down(self):
        y_new = self.ycor() - 20
        self.goto(self.xcor(), y_new)
