# Henny Brenden, Kasper. S Karlsen

import math
import turtle


class Rectangle:
    def __init__(self, x0, y0, x1, y1, *, color="black", linewidth=2):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.color = color
        self.linewidth = linewidth

    def width(self):
        return self.x1 - self.x0

    def height(self):
        return self.y1 - self.y0

    def area(self):
        return self.width() * self.height()

    def move(self, dx, dy):
        self.x0 += dx; self.x1 += dx
        self.y0 += dy; self.y1 += dy

    def info(self):
        print(
            f"Rectangle | ll=({self.x0}, {self.y0}), ur=({self.x1}, {self.y1}), "
            f"w={self.width()}, h={self.height()}, area={self.area()}, "
            f"color={self.color}, linewidth={self.linewidth}"
        )

    def draw(self, t):
        # husk gjeldende stil så vi ikke saboterer andres figurer
        old_color, old_size = t.pencolor(), t.pensize()
        t.pencolor(self.color)
        t.pensize(self.linewidth)

        t.penup()
        t.goto(self.x0, self.y0)
        t.pendown()
        for _ in range(2):
            t.forward(self.width())
            t.left(90)
            t.forward(self.height())
            t.left(90)

        t.pencolor(old_color)
        t.pensize(old_size)


class Triangle:
    def __init__(self, p1, p2, p3, *, color="black", linewidth=2):
        """p1, p2, p3 er tupler (x, y)."""
        self.p1, self.p2, self.p3 = p1, p2, p3
        self.color = color
        self.linewidth = linewidth

    def area(self):
        # Shoelace-formelen. Dette er faktisk matte, ikke svart magi.
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

    def info(self):
        print(
            f"Triangle | p1={self.p1}, p2={self.p2}, p3={self.p3}, "
            f"area={self.area()}, color={self.color}, linewidth={self.linewidth}"
        )

    def draw(self, t):
        old_color, old_size = t.pencolor(), t.pensize()
        t.pencolor(self.color)
        t.pensize(self.linewidth)

        t.penup(); t.goto(*self.p1); t.pendown()
        t.goto(*self.p2)
        t.goto(*self.p3)
        t.goto(*self.p1)

        t.pencolor(old_color)
        t.pensize(old_size)


class Circle:
    def __init__(self, cx, cy, r, *, color="black", linewidth=2, segments=120):
        self.cx, self.cy, self.r = cx, cy, r
        self.color = color
        self.linewidth = linewidth
        self.segments = max(12, int(segments))  # ikke vær gjerrig på kanter

    def info(self):
        print(
            f"Circle | center=({self.cx}, {self.cy}), r={self.r}, "
            f"color={self.color}, linewidth={self.linewidth}, segments={self.segments}"
        )

    def draw(self, t):
        old_color, old_size = t.pencolor(), t.pensize()
        t.pencolor(self.color)
        t.pensize(self.linewidth)

        n = self.segments
        step = 2 * math.pi * self.r / n       # side-lengde i polygonet
        turn = 360 / n

        # start på høyresiden av sirkelen
        t.penup()
        t.goto(self.cx + self.r, self.cy)
        t.setheading(90)  # pek oppover for litt penere start, valgfritt
        t.pendown()

        for _ in range(n):
            t.forward(step)
            t.left(turn)

        t.pencolor(old_color)
        t.pensize(old_size)


def draw_fitting_square_for_circle(circ, *, color="gray", linewidth=1):
    """Returner et Rectangle som akkurat omslutter sirkelen."""
    side = 2 * circ.r
    return Rectangle(
        circ.cx - circ.r, circ.cy - circ.r,
        circ.cx + circ.r, circ.cy + circ.r,
        color=color, linewidth=linewidth
    )


if __name__ == "__main__":
    # Lag en felles turtle
    t = turtle.Turtle()
    t.speed(0)

    # Diverse rektangler og trekanter med ulike farger/tykkelser
    shapes = [
        Rectangle(0, 0, 140, 80, color="steel blue", linewidth=3),
        Rectangle(-200, -120, -80, -40, color="firebrick", linewidth=4),
        Triangle((50, 150), (140, 220), (20, 230), color="dark green", linewidth=3),
        Triangle((-150, 60), (-80, 160), (-220, 170), color="purple", linewidth=2),
        Rectangle(-20, 100, -110, 50, color="orange", linewidth=5),
    ]

    # Sirkel + kvadrat som den akkurat passer i (kontroll på korrekt tegning)
    c = Circle(0, -170, 60, color="orange", linewidth=3, segments=150)
    shapes.extend([c])

    # Skriv info og tegn alt
    for s in shapes:
        s.info()
        s.draw(t)

    turtle.done()