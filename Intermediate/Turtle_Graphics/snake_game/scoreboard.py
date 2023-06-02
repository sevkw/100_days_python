from turtle import Turtle

FONT = ("Verdana", 12, "bold")
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.refresh_scoreboard()
    
    def refresh_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.refresh_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", move=False, align=ALIGN, font=FONT)