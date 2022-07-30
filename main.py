import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed_states = []
score = 0

while len(guessed_states) < 50:
    states = pandas.read_csv("50_states.csv")
    all_states = states.state.tolist()
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        score += 1
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_data = states[states.state == answer_state]
        new_state.goto(float(state_data.x), float(state_data.y))
        new_state.write(answer_state)
