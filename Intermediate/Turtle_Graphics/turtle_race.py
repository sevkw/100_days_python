from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

starting_x = -230
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_y = [180, 120, 60, 0, -60, -120]

race_turtles = []

for t_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=starting_x, y=starting_y[t_index])
    race_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in race_turtles:
                
        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()