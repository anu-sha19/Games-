from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 280)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Arial", 30, 'normal'))
