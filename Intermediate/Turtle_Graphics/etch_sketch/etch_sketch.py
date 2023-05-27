from turtle import Turtle, Screen

DIS = 20

def move_forward():
    """Move the turtle forward by input distance."""
    sketcher.fd(DIS)

def move_backward():
    """Move the turtle backward by input distance"""
    sketcher.bk(DIS)

def turn_right():
    """Move the turtle clockwize by input angle."""
    sketcher.rt(DIS)

def turn_left():
    """Move the turtle counter-clockwize by input angle."""
    sketcher.lt(DIS)

def clear_drawing():
    """Clear the drawings and return the turtle back to center."""
    sketcher.reset()

key_funs = {'w':move_forward
            , 's':move_backward
            , 'd':turn_right
            , 'a':turn_left
            , 'c':clear_drawing
            }


sketcher = Turtle()
sketcher.pensize(5)
screen = Screen()

screen.listen()

for k in key_funs:
    screen.onkey(key=k, fun=key_funs[k])

screen.exitonclick()