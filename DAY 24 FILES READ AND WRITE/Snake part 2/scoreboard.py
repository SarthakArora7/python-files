from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.show_score()

    def show_score(self):
        self.clear()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.write(f"Score = {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def point(self):
        self.score = self.score + 1
        self.show_score()

    def reset_score(self):
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        if self.score > self.high_score:
            with open("data.txt", "w") as file:
                self.high_score = int(file.write(f"{self.score}"))
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGN, font=FONT)

