from turtle import Turtle, done



def generate_lsystem(axiom, rules, n):
    result = axiom
    for _ in range(n):
        next_result = ""
        for char in result:
            next_result += rules.get(char, char)
        result = next_result
    return result

def draw_lsystem(t, instructions, length, angle):
    for cmd in instructions:
        if cmd in ("A", "B"):
            t.forward(length)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)


def draw_curve(rules, start, angle, iterations, length):
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    instructions = generate_lsystem(start, rules, iterations)
    draw_lsystem(t, instructions, length, angle)

    done()
