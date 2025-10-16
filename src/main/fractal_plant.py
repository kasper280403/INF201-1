from turtle import Turtle, done, Screen

def start():
    start = "X"
    angle = 20
    depth = 5
    length = 3

    instructions = start
    for i in range(0, depth):
        instructions = generate_instructions(instructions)

    draw(instructions, length, angle)


def generate_instructions(instructions):
    new_instructions = ""
    for char in instructions:
        if char == "X":
            new_instructions += "F-[[X]+X]+F[+FX]-X"
        elif char == "F":
            new_instructions += "FF"
        else:
            new_instructions += char

    return new_instructions

def draw(instructions, length, angle):
    t = Turtle()
    screen = Screen()
    screen.tracer(0)
    t.speed(0)
    t.color("green")
    t.penup()
    t.goto(0, -100)
    t.left(90)
    t.pendown()

    pos = []
    dir = []
    for char in instructions:
        if char == "F":
            t.forward(length)
        elif char == "[":
            pos.append(t.position())
            dir.append(t.heading())
        elif char == "]":
            t.penup()
            t.goto(pos[-1][0], pos[-1][1])
            t.setheading(dir[-1])
            pos.pop()
            dir.pop()
            t.pendown()
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)

    screen.update()
    done()


