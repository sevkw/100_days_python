from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PINK Snake Game")
# turn off the animation using tracer(0)
screen.tracer(0)

## create starting snake body
## As 3 white squares with 20*20 pixels each

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for t in range(0, 3):
    new_segment = Turtle(shape="square")
    new_segment.color("pink")
    new_segment.penup()
    new_segment.setpos(starting_positions[t])
    segments.append(new_segment)


## to move the starting segments

game_is_on = True

while game_is_on:
    # allow the snake segments to move forward at the same time
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    
screen.exitonclick()