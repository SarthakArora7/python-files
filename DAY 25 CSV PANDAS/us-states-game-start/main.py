import turtle
from turtle import Screen, Turtle

import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()

missing_states = []
answered_state = []
while len(answered_state) < 50:
    answer_state = screen.textinput(title=f"{len(answered_state)}/50 State's Correct", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        [missing_states.append(state) for state in all_states if state not in answered_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        answered_state.append(answer_state)
        state_data = data[data.state == answer_state]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


turtle.mainloop()
