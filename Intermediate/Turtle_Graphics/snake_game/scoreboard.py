from turtle import Turtle

FONT = ("Verdana", 12, "bold")
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.refresh_scoreboard()
    
    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.refresh_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        ## to reset the score for the game instance to 0
        self.score = 0
        self.refresh_scoreboard()