from turtle import Turtle, Screen
import random
import numpy as np
timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(80)
# ------------------------------------------------------------------------------------
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
# ------------------------------------------------------------------------------------
# for i in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
# -------------------------------------------------------------------------------------
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

# for j in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     for i in range(j):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360 / j)


# Random Walk.
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

for i in range(10):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()