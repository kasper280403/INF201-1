# Deliverable 2 - INF201
# Henny Brenden, Kasper S. Karlsen

# Rectangle-klassen er opprinnelig basert på eksemplet fra INF201 (Lecture 8)

import turtle
import math
import random


class Rectangle:
    def __init__(self, x0, y0, x1, y1, color="black", linewidth=2):
        """
        x0, y0: ett hjørne
        x1, y1: motsatt hjørne
        """
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.color = color
        self.linewidth = linewidth

    def control_corners(self):
        self.x0, self.x1 = sorted([self.x0, self.x1])
        self.y0, self.y1 = sorted([self.y0, self.y1])

    def width(self):
        return self.x1 - self.x0

    def height(self):
        return self.y1 - self.y0

    def area(self):
        return self.width() * self.height()

    def move(self, dx, dy):
        self.x0 += dx
        self.x1 += dx
        self.y0 += dy
        self.y1 += dy

    def info(self):
        self.control_corners()
        print(
            f"Rectangle | "
            f"lower left=({self.x0}, {self.y0}), "
            f"upper right=({self.x1}, {self.y1}), "
            f"width={self.width()}, height={self.height()}, "
            f"area={self.area()}, "
            f"color={self.color}, linewidth={self.linewidth}"
        )

    def draw(self, t):
        old_color, old_size = t.pencolor(), t.pensize()

        t.pencolor(self.color)
        t.pensize(self.linewidth)

        self.control_corners()

        w = self.width()
        h = self.height()

        t.penup()
        t.goto(self.x0, self.y0)
        t.setheading(0)
        t.pendown()

        for _ in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)

        t.penup()
        t.pencolor(old_color)
        t.pensize(old_size)


class Triangle:
    def __init__(self, p1, p2, p3, color="black", linewidth=2):
        """
        p1, p2, p3: hjørnene til trekanten, hver som (x, y)
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.linewidth = linewidth

    def side_length(self, a, b):
        ax, ay = a
        bx, by = b
        return math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)

    def area(self):
        a = self.side_length(self.p1, self.p2)
        b = self.side_length(self.p2, self.p3)
        c = self.side_length(self.p3, self.p1)
        s = 0.5 * (a + b + c)
        A = math.sqrt(max(s * (s - a) * (s - b) * (s - c), 0))
        return A

    def info(self):
        print(
            f"Triangle | "
            f"p1={self.p1}, p2={self.p2}, p3={self.p3}, "
            f"area={self.area()}, "
            f"color={self.color}, linewidth={self.linewidth}"
        )

    def draw(self, t):
        old_color, old_size = t.pencolor(), t.pensize()

        t.pencolor(self.color)
        t.pensize(self.linewidth)

        (x1, y1) = self.p1
        (x2, y2) = self.p2
        (x3, y3) = self.p3

        t.penup()
        t.goto(x1, y1)
        t.setheading(0)
        t.pendown()

        t.goto(x2, y2)
        t.goto(x3, y3)
        t.goto(x1, y1)

        t.penup()
        t.pencolor(old_color)
        t.pensize(old_size)


class Circle:
    def __init__(self, cx, cy, r, color="black", linewidth=2, segments=120):
        """
        cx, cy: sentrum
        r: radius
        color: linjefarge
        linewidth: tykkelse på strek
        segments: hvor mange linjebiter vi bruker for å tegne sirkelen
        """
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color
        self.linewidth = linewidth
        self.segments = max(12, int(segments)) 

    def circumference(self):
        return 2 * math.pi * self.r

    def info(self):
        print(
            f"Circle | "
            f"center=({self.cx}, {self.cy}), r={self.r}, "
            f"circumference≈{self.circumference():.2f}, "
            f"color={self.color}, linewidth={self.linewidth}, "
            f"segments={self.segments}"
        )

    def draw(self, t):
        old_color, old_size = t.pencolor(), t.pensize()
        t.pencolor(self.color)
        t.pensize(self.linewidth)

        pts = []
        for i in range(self.segments + 1):
            angle = 2 * math.pi * i / self.segments
            x = self.cx + self.r * math.cos(angle)
            y = self.cy + self.r * math.sin(angle)
            pts.append((x, y))

        t.penup()
        t.goto(pts[0][0], pts[0][1])
        t.setheading(0)
        t.pendown()
        for (x, y) in pts[1:]:
            t.goto(x, y)
        t.penup()

        t.pencolor(old_color)
        t.pensize(old_size)


def get_linewidth():
    """Random linewidth."""
    r = random.randint(1, 5)
    if r < 4:
        r = r * random.randint(1, 2)
    return r


def get_color():
    """Random colors."""
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
    return Rectangle(
        x0, y0, x1, y1,
        color=get_color(),
        linewidth=get_linewidth()
    )


def create_circle_random(area, r_range):
    x_min, y_min, x_max, y_max = area
    r_min, r_max = r_range

    r = random.randint(r_min, r_max)
    cx = random.randint(x_min + r, x_max - r)
    cy = random.randint(y_min + r, y_max - r)

    return Circle(
        cx, cy, r,
        color=get_color(),
        linewidth=get_linewidth()
    )


def create_triangle_random(area):
    x_min, y_min, x_max, y_max = area

    p1 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p2 = (random.randint(x_min, x_max), random.randint(y_min, y_max))
    p3 = (random.randint(x_min, x_max), random.randint(y_min, y_max))

    return Triangle(
        p1, p2, p3,
        color=get_color(),
        linewidth=get_linewidth()
    )


def setup_screen():
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.title("INF201 Deliverable 2")
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


if __name__ == "__main__":
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
        rect.info()
    for circ in circles:
        circ.info()
    for tri in triangles:
        tri.info()

    for rect in rectangles:
        rect.draw(turt)
    for circ in circles:
        circ.draw(turt)
    for tri in triangles:
        tri.draw(turt)

    test_r = 60
    test_cx = 0
    test_cy = 0

    test_circle = Circle(
        test_cx,
        test_cy,
        test_r,
        color="black",
        linewidth=3,
    )

    test_square = Rectangle(
        test_cx - test_r,
        test_cy - test_r,
        test_cx + test_r,
        test_cy + test_r,
        color="black",
        linewidth=1,
    )

    test_circle.info()
    test_square.info()

    test_circle.draw(turt)
    test_square.draw(turt)

    window.update()
    window.mainloop()
    turtle.done()