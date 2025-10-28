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

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3], get_color(), get_linewidth())
    rectangle.control_corners()
    return rectangle

def create_circle_random(area, r_range):
    x_min, y_min, x_max, y_max = area
    r_min, r_max = r_range

    r = random.randint(r_min, r_max)
    cx = random.randint(x_min + r, x_max - r)
    cy = random.randint(y_min + r, y_max - r)

    return Circle(cx, cy, r, get_color(), get_linewidth())

def create_triangle_random(area):
    x_min, y_min, x_max, y_max = area

    p1 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p2 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p3 = (random.randint(x_min, x_max), random.randint(y_min, y_max))


    return Triangle(p1, p2, p3, get_color(), get_linewidth())

def create_turtle():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(0)

    return t

def get_linewidth():
    r = random.randint(1, 5)
    if r < 4:
        r = r * random.randint(1, 2)

    return r

def get_color():
    colors = [
        "red",
        "green",
        "blue",
        "yellow",
        "magenta",
        "cyan",
        "black",
        "orange",
        "purple",
        "brown",
        "pink",
        "lime",
        "navy",
        "gray",
        "gold"
    ]

    return colors[random.randint(0, len(colors) - 1)]



if __name__ == "__main__":
    #xMin, yMin, xMax, yMax
    draw_area = [-300, -300, 300, 300]

    rectangles = []
    circles = []
    triangles = []

    for _ in range(3):


        rectangles.append(create_random_rectangle(draw_area))
        circles.append(create_circle_random(draw_area, [20, 100]))
        triangles.append(create_triangle_random(draw_area))


    for r in rectangles:
        r.info()

    t = create_turtle()
    t.screen.tracer(0)
    for r in rectangles:
        r.draw(t)
    for tri in triangles:
        tri.draw(t)
    for c in circles:
        c.draw(t)

    t.screen.update()
    turtle.done()
