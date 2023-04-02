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
    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_data = data[data.state == answer_state]
        new_state.goto(int(state_data.x), int(state_data.y))
        # new_state.write(state_data.state.item())
        new_state.write(answer_state)


# make the screen open always
turtle.mainloop()


