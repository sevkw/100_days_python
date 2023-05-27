import turtle as t
from random import randint

spiral = t.Turtle()
screen = t.Screen()
screen.colormode(255)


def draw_spiralgraph(gap):
    for angle in range(0, 360, gap):
        spiral.speed("fastest")
        spiral.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        spiral.circle(50)
        spiral.settiltangle(0)
        spiral.setheading(angle)


draw_spiralgraph(10)

screen.exitonclick()
