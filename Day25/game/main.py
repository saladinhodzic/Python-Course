import turtle
import pandas
# making the screen
screen = turtle.Screen()
screen.addshape("blank_states_img.gif")
# turtle
map = turtle.Turtle("blank_states_img.gif")

# getting data
data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()
# keeping track of correct guesses
score = 0
correct_guesses = []
missing_states=[]
# checking answer
game_is_on = True
while game_is_on:
    user_input = screen.textinput(title=f"Score {score}/50",prompt="Guess the state:").title()
    if user_input == "Exit":
        for state in states:
            if state not in correct_guesses:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    for state in states:
        if user_input == state and user_input not in correct_guesses:
            add_state = turtle.Turtle()
            row = data[data["state"] == user_input]
            add_state.hideturtle()
            add_state.penup()
            add_state.color("black")
            add_state.goto(int(row["x"]),int(row["y"]))
            add_state.write(f"{user_input}")
            correct_guesses.append(user_input)
            score+=1








