# Henny Brenden, Kasper S. Karlsen

class Triangle:
    def __init__(self, p1, p2, p3, color="black", linewidth=2):
        """p1, p2, p3 er tupler (x, y)."""
        self.p1, self.p2, self.p3 = p1, p2, p3
        self.color = color
        self.linewidth = linewidth

    def area(self):
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