# Henny Brenden, Kasper S. Karlsen

import random
import turtle

from src.main.del2.Circle import Circle
from src.main.del2.drawing import Rectangle


def create_random_rectangle(area):
    xMin = area[0]
    yMin = area[1]
    xMax = area[2]
    yMax = area[3]

    random_list = []
    for i in range(2):
        random_list.append(random.randint(xMin, xMax))
        random_list.append(random.randint(yMin, yMax))

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3])
    rectangle.control_corners()
    return rectangle

def create_circle_random(area, r_range):
    for a in area:
        if a < 0:
            a = a + r_range[1]
        else:
            a = a - r_range[1]

    cx, cy = random.randint(area[0], area[2]), random.randint(area[1], area[3])
    r = random.randint(r_range[0], r_range[1])

    circle = Circle(cx, cy, r)

    return circle

def create_turtle():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(0)

    return t


if __name__ == "__main__":
    #xMin, yMin, xMax, yMax
    draw_area = [-300, -300, 300, 300]

    rectangles = []
    circles = []

    for _ in range(3):
        rectangles.append(create_random_rectangle(draw_area))
        circles.append(create_circle_random(draw_area, [20, 100]))

    for r in rectangles:
        r.info()

    t = create_turtle()

    for r in rectangles:
        r.draw(t)
    for c in circles:
        c.draw(t)

    turtle.done()


