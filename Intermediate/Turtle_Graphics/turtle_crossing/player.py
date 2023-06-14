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
        self.finish_line = FINISH_LINE_Y
    
    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    
    def is_at_finish_line(self):
        if self.ycor() > self.finish_line:
            return True
        else:
            return False