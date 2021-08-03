from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.setposition(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.setposition(0 ,0)
    #     self.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))








