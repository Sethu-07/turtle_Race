import turtle
from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tim = Turtle(shape="turtle")
tim.color(colors[0])
tim.penup()
tim.goto(x=-230, y=-100)

tim2 = Turtle(shape="turtle")
tim2.color(colors[1])
tim2.penup()
tim2.goto(x=-230, y=-60)

tim3 = Turtle(shape="turtle")
tim3.color(colors[2])
tim3.penup()
tim3.goto(x=-230, y=-20)

tim4 = Turtle(shape="turtle")
tim4.color(colors[3])
tim4.penup()
tim4.goto(x=-230, y=20)

tim5 = Turtle(shape="turtle")
tim5.color(colors[4])
tim5.penup()
tim5.goto(x=-230, y=60)

tim6 = Turtle(shape="turtle")
tim6.color(colors[5])
tim6.penup()
tim6.goto(x=-230, y=100)

turtles = [tim, tim2, tim3, tim4, tim5, tim6]
if user_bet:
    is_on = True

while is_on:

    for turtless in turtles:
        if turtless.xcor() > 230:
            is_on = False
            winning_color = turtless.pencolor()
            if winning_color == user_bet:
                print(f"You've won.The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost.The {winning_color} turtle is the winner!")
        turtless.forward(random.randint(0, 10))


turtle.done()
