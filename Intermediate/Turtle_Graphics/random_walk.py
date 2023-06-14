import turtle as t
from random import randint
from random import choice
def random_direction(turtle):
    """A function to randomnize the heading direction."""
    direction_angle = [0, 90, 180, 270]
    to_angle = choice(direction_angle)
    turtle.setheading(to_angle)


rt = t.Turtle()
rt.pensize(5)
rt.speed("fast")
screen = t.Screen()
screen.colormode(255)

for _ in range(200):
    random_direction(rt)
    rt.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    rt.forward(20)

screen.exitonclick()
