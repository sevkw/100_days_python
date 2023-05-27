import colorgram
import turtle as t
from random import choice

def extract_colors(image, num_colors):
    """Return the rgb of extracted colors from a given image."""
    colors = colorgram.extract(image, num_colors)
    rgb_list = []
    for c in colors:
        r = c.rgb.r
        g = c.rgb.g
        b = c.rgb.b
        rgb_list.append((r, g, b))

    return rgb_list


def draw_dots(dotsize, dotperrow, num_colors):
    """Paints the dotsize in pixels using num_colors on a canvas determined by the dotperrow."""
    color_list = extract_colors('image.jpeg', num_colors)
    screen_width = int(dotperrow*dotsize*2)
    screen_height = screen_width
    screen = t.Screen()
    screen.setworldcoordinates(0, 0, int(screen_width - dotsize - dotsize/2), int(screen_height - dotsize - dotsize/2))
    screen.colormode(255)

    dotty = t.Turtle()
    dotty.speed('fastest')
    dotty.pen(shown=False)
    
    row = 0

    for _ in range(dotperrow):
        for _ in range(dotperrow):
            dot_color = choice(color_list)
            dotty.penup()
            dotty.dot(dotsize, dot_color)
            dotty.forward(dotsize)
            dotty.forward(dotsize)
        row += 1
        dotty.goto(0, row*dotsize*2)
    
    screen.exitonclick()

        

draw_dots(20, 10, 20)


