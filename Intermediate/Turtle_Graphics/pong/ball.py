from turtle import Turtle
import random

MOVE_DISTANCE = 20
ORIGINAL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.starting_position = (0, 0)
        self.goto(self.starting_position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = ORIGINAL_SPEED
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def reset_position(self):
        self.goto(self.starting_position)
        self.move_speed = ORIGINAL_SPEED
        # when a paddle misses the bounce, the ball would goes to the opposite paddle
        self.bounce_x()
    
