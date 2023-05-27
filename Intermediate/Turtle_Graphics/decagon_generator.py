import turtle as t
from random import randint

tagon = t.Turtle()

sides = 3
angle = 360
angle_taken = 0
sides_drawn = 0
screen = t.Screen()
screen.colormode(255)

while sides < 11:
    tagon.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    while sides_drawn < sides:
        tagon.forward(20)
        sides_drawn += 1
        tagon.right(angle / sides)
    sides += 1
    sides_drawn = 0

screen.exitonclick()