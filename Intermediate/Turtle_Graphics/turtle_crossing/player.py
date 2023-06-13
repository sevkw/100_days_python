STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setposition(STARTING_POSITION)
        self.color("black")
        self.setheading(90)
    
    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
