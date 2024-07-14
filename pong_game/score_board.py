from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_board()

    def update_board(self):
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(200, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_score(self, direction):
        if direction == 'r':
            self.r_score += 1
        else:
            self.l_score += 1
        self.clear()
        self.update_board()

    def winner(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Courier", 50, "normal"))



