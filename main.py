from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race: \n Red, Orange, Yellow, Green, Blue Or Purple").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -90
all_turtles = []

positions = [-46, -120, -146, -227, -217, 20, 53, 204, -136, -18]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
cars = []

for color in colors:
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(color)
    new_turtles.penup()
    new_turtles.goto(x=-280, y=y)
    all_turtles.append(new_turtles)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                turtle.write(
                    f"You've won! The {winning_color} turtle is the winner!",
                    align='right',
                    font=('Arial', 20, 'normal')
                )
            else:
                turtle.write(
                    f"You've lost! The {winning_color} turtle is the winner!",
                    align='right',
                    font=('Arial', 20, 'normal')
                )

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
