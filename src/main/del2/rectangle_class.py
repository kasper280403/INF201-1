# Henny Brenden, Kasper S. Karlsen

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
        """Move rectangle by dx and dy."""
        self.x0 += dx
        self.x1 += dx
        self.y0 += dy
        self.y1 += dy

    def info(self):
        """Print coordinates of the rectangle corners."""
        print(f"Lower left: ({self.x0}, {self.y0}), upper right: ({self.x1}, {self.y1})")

if __name__ == "__main__":
    rectangles = [
        Rectangle(0, 0, 2, 3),
        Rectangle(1, 1, 4, 5),
        Rectangle(-2, -1, 1, 2)
    ]

    for r in rectangles:
        r.info()