#Kasper S Karlsen, Henny Brenden

from turtle import Turtle, Screen

def complete_flake(t, depth):
    if depth == 0:
        t.forward(10)
    else:
        complete_flake(t, depth - 1)
        t.left(60)
        complete_flake(t, depth - 1)
        t.right(60)
        t.right(60)
        complete_flake(t, depth - 1)
        t.left(60)
        complete_flake(t, depth - 1)



def draw_flake(depth):
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 0)
    t.pendown()

    for _ in range(depth):
        complete_flake(t, depth)
        t.right(120)

    Screen().exitonclick()