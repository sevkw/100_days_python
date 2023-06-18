FONT = ("Courier", 12, "normal")

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load Image to the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# make answer turtle
show_answer = turtle.Turtle()
show_answer.hideturtle()
show_answer.penup()

correct_guess = 0

past_guesses = []

states_data = pd.read_csv("50_states.csv", header=0)

is_game_finished = False

while not is_game_finished:

    if correct_guess == 0:
        answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?").title()

    states_data = pd.read_csv("50_states.csv", header=0)

    match_state = states_data[states_data.state == answer_state]

    if answer_state in states_data.values and not answer_state in past_guesses:
        past_guesses.append(answer_state)
        match_state_x = int(match_state.x.iloc[0])
        match_state_y = int(match_state.y.iloc[0])
        show_answer.goto(match_state_x, match_state_y)
        show_answer.write(answer_state, move=False, align='center', font=FONT)
        correct_guess += 1
    
    if answer_state == 'Exit':
        missed_state = states_data[~states_data.state.isin(past_guesses)]
        missed_state.state.to_csv("study_list.csv")
        break
    
    if correct_guess == 50:
        is_game_finished = False

# generate a new file that contains the list of states NOT yet guessed by the user


# screen.exitonclick()

## Below are code for getting the x,y for each state in the image
# when using need to comment out screen.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()