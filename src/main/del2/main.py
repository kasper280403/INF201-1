# Henny Brenden, Kasper S. Karlsen

import random
import turtle

from src.main.del2.Circle import Circle
from src.main.del2.drawing import Rectangle
from src.main.del2.Triangle import Triangle


def create_random_rectangle(area):
    x_min, y_min, x_max, y_max = area

    random_list = []
    for i in range(2):
        random_list.append(random.randint(x_min, x_max))
        random_list.append(random.randint(y_min, y_max))

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3])
    rectangle.control_corners()
    return rectangle

def create_circle_random(area, r_range):
    x_min, y_min, x_max, y_max = area
    r_min, r_max = r_range

    r = random.randint(r_min, r_max)
    cx = random.randint(x_min + r, x_max - r)
    cy = random.randint(y_min + r, y_max - r)

    return Circle(cx, cy, r)

def create_triangle_random(area):
    xMin = area[0]
    yMin = area[1]
    xMax = area[2]
    yMax = area[3]

    t1 = (random.randint(xMin, xMax), random.randint(yMin, yMax))
    t2 = (random.randint(xMin, xMax), random.randint(yMin, yMax))
    t3 = (random.randint(xMin, xMax), random.randint(yMin, yMax))

    return Triangle(t1, t2, t3)


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
    triangles = []

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
    for t in triangles:
        t.draw(t)

    turtle.done()
