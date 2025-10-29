# Henny Brenden, Kasper S. Karlsen

import random
import turtle

from Circle import Circle
from drawing import Rectangle
from Triangle import Triangle

def get_linewidth():
    r = random.randint(1, 5)
    if r < 4:
        r = r * random.randint(1, 2)
    return r


def get_color():
    colors = [
        "red", "green", "blue", "yellow",
        "magenta", "cyan", "black", "orange",
        "purple", "brown", "pink", "lime",
        "navy", "gray", "gold"
    ]
    return colors[random.randint(0, len(colors) - 1)]


def create_random_rectangle(area):
    x_min, y_min, x_max, y_max = area
    x0 = random.randint(x_min, x_max)
    y0 = random.randint(y_min, y_max)
    x1 = random.randint(x_min, x_max)
    y1 = random.randint(y_min, y_max)
    return Rectangle(x0, y0, x1, y1, color=get_color(), linewidth=get_linewidth())


def create_circle_random(area, r_range):
    x_min, y_min, x_max, y_max = area
    r_min, r_max = r_range

    r = random.randint(r_min, r_max)
    cx = random.randint(x_min + r, x_max - r)
    cy = random.randint(y_min + r, y_max - r)
    return Circle(cx, cy, r, color=get_color(), linewidth=get_linewidth())


def create_triangle_random(area):
    x_min, y_min, x_max, y_max = area

    p1 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p2 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p3 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    return Triangle(p1, p2, p3, color=get_color(), linewidth=get_linewidth())


def setup_screen():
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.title("INF201 tegning :)")
    window.tracer(0)
    return window


def create_turtle():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    return t


def make_sub_areas(xmin, ymin, xmax, ymax, n):
    width_total = xmax - xmin
    width_each = width_total / n
    areas = []
    for i in range(n):
        sxmin = int(xmin + i * width_each)
        sxmax = int(xmin + (i + 1) * width_each)
        areas.append((sxmin, ymin, sxmax, ymax))
    return areas

# main
window = setup_screen()
turt = create_turtle()

rect_area = (-380, -250, -130, 250)
circle_area = (-120, -250, 120, 250)
tri_area = (130, -250, 380, 250)

N = 3

rect_subareas = make_sub_areas(*rect_area, N)
rectangles = [
    create_random_rectangle(a)
    for a in rect_subareas
]

circles = [
    create_circle_random(circle_area, (20, 80))
    for _ in range(N)
]

triangles = [
    create_triangle_random(tri_area)
    for _ in range(N)
]

for rect in rectangles:
    rect.draw(turt)
for circ in circles:
    circ.draw(turt)
for tri in triangles:
    tri.draw(turt)

window.update()
window.mainloop()
turtle.done()