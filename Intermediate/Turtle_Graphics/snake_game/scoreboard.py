from turtle import Turtle

FONT = ("Verdana", 12, "bold")
ALIGN = 'center'

with open("game_data.txt", mode='r') as data:
    HIGH_SCORE = data.read()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE)
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

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("game_data.txt", mode="w") as write_data:
                write_data.write(f"{self.high_score}")
                write_data.close()
        ## to reset the score for the game instance to 0
        self.score = 0
        self.refresh_scoreboard()