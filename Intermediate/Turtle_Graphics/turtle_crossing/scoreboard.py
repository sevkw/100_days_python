FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color('black')
        self.penup()
        self.goto(-250, 250)
        self.refresh_scoreboard()
    
    def refresh_scoreboard(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)
    
    def update_level(self):
        self.clear()
        self.level += 1
        self.refresh_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
