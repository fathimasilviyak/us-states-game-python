import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state's name? ").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_data = data[data.state == answer_state]
        new_state.goto(int(state_data.x), int(state_data.y))
        # new_state.write(state_data.state.item())
        new_state.write(answer_state)

