# Henny Brenden, Kasper S. Karlsen

class Rectangle:
    def __init__(self, x0, y0, x1, y1, color="black", linewidth=2):
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

    def info(self):
        """Print coordinates of the rectangle corners."""
        print(
            f"Rectangle | lower left=({self.x0}, {self.y0}), "
            f"upper right=({self.x1}, {self.y1}), "
            f"color={self.color}, linewidth={self.linewidth}, "
            f"width={self.width()}, height={self.height()}, area={self.area()}"
        )