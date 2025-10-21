# Henny Brenden, Kasper S. Karlsen

import turtle

class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def width(self):
        return self.x1 - self.x0

    def height(self):
        return self.y1 - self.y0

    def area(self):
        return self.width() * self.height()

    def move(self, dx, dy):
        """Flytt rektanglene etter dx og dy."""
        self.x0 += dx
        self.x1 += dx
        self.y0 += dy
        self.y1 += dy

    def info(self):
        """Print kordinatene til rektanglenes hjørner"""
        print(f"Lower left: ({self.x0}, {self.y0}), upper right: ({self.x1}, {self.y1})")

    def draw(self, t):
        """Tegn rektanglene."""
        t.penup()
        t.goto(self.x0, self.y0)
        t.pendown()

        for _ in range(2):
            t.forward(self.width())
            t.left(90)
            t.forward(self.height())
            t.left(90)


if __name__ == "__main__":
    # lag rektanglene
    rectangles = [
        Rectangle(0, 0, 100, 50),
        Rectangle(120, 20, 200, 100),
        Rectangle(-80, -50, 20, 30)
    ]

    # lag turtle for å tegne
    t = turtle.Turtle()
    t.speed(2)

    # tegn alle rektanglene
    for r in rectangles:
        r.draw(t)

    turtle.done()