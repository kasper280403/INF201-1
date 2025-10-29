# Henny Brenden, Kasper S. Karlsen

import random
import turtle

from src.main.del2.Circle import Circle
from src.main.del2.drawing import Rectangle
from src.main.del2.Triangle import Triangle


def create_random_rectangle(area):
    x_min, y_min, x_max, y_max = area
<<<<<<< HEAD

    random_list = []
    for i in range(2):
        random_list.append(random.randint(x_min, x_max))
        random_list.append(random.randint(y_min, y_max))

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3], get_color(), get_linewidth())
    rectangle.control_corners()
    return rectangle
=======
    x0 = random.randint(x_min, x_max)
    y0 = random.randint(y_min, y_max)
    x1 = random.randint(x_min, x_max)
    y1 = random.randint(y_min, y_max)
    return Rectangle(x0, y0, x1, y1, color=color, linewidth=linewidth)
>>>>>>> 18b7eac (Fikset småfeil i drawing og feil i main, så nå fungerer koden perfekt)

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


<<<<<<< HEAD
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
=======

window = setup_screen()
turt = create_turtle()

rect_area  = (-380, -250, -130, 250)
circle_area = (-120, -250,  120, 250)
tri_area = ( 130, -250,  380, 250)

N = 3

rect_subareas   = make_sub_areas(*rect_area, N)
rectangles = [
    create_random_rectangle(a, color="red", linewidth=2)
    for a in rect_subareas
]

circle_subareas = make_sub_areas(*circle_area, N)
circles = [
    create_circle_random(circle_area, (20, 80), color="blue", linewidth=2)
    for _ in range(N)
]
>>>>>>> 18b7eac (Fikset småfeil i drawing og feil i main, så nå fungerer koden perfekt)

tri_subareas    = make_sub_areas(*tri_area, N)
triangles = [
    create_triangle_random(tri_area, color="green", linewidth=2)
    for _ in range(N)
]

<<<<<<< HEAD
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
=======
for rect in rectangles:
    rect.draw(turt)
for circ in circles:
    circ.draw(turt)
for tri in triangles:
    tri.draw(turt)

window.update()
window.mainloop()
turtle.done()
>>>>>>> 18b7eac (Fikset småfeil i drawing og feil i main, så nå fungerer koden perfekt)
