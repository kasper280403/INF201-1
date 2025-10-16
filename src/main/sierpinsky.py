from turtle import Turtle, Screen

def dragon(turtle, depth):
    turtle.forward(10)  # F
    dragonX(turtle, depth - 1)  # X


def dragonX(turtle, depth):
    if depth > 0:  # X ->
        dragonX(turtle, depth - 1)  # X
        turtle.left(90)  # +
        dragonY(turtle, depth - 1)  # Y
        turtle.forward(10)  # F


def dragonY(turtle, depth):
    if depth > 0:  # Y ->
        turtle.forward(10)  # F
        dragonX(turtle, depth - 1)  # X
        turtle.right(90)  # -
        dragonY(turtle, depth - 1)  # Y

t = Turtle()
dragon(t, 10)