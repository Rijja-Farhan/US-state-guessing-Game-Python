from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.addshape("blank_states_img.gif")

turtle = Turtle()
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states_list = data["state"].tolist()
total = len(states_list)
count = 0
game_is_on = True
states_guessed=[]
learn_states =[]
print(states_list)
while game_is_on:
    entered_state = screen.textinput(title="Guess the state   "+ str(count) + "/ 50", prompt="Enter the state: ").title()#to convert it into country name type
    if entered_state in states_list:
        count=+1
        turtle1 =Turtle()
        turtle1.hideturtle()
        turtle1.penup()
        found_state = data[data["state"] == entered_state]
        x_axis = int(found_state["x"].iloc[0])
        y_axis =int(found_state["y"].iloc[0])
        turtle1.goto(x_axis,y_axis)
        turtle1.write(entered_state)
        states_guessed.append(entered_state)
    elif entered_state == "Exit":
        for states in states_list:
            if states in states_guessed:
                pass
            else:
                learn_states.append(states)
        df = pd.DataFrame({"State": learn_states})
        filename = "learn_states.csv"

        # Save the DataFrame to a CSV file
        df.to_csv(filename)

        game_is_on =False

