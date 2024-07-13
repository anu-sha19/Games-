FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = level
        self.goto(-220, 260)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)



