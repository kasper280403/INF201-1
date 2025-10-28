# Henny Brenden, Kasper S. Karlsen

class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def control_corners(self):
        if self.x0 > self.x1:
            temp = self.x0
            self.x0 = self.x1
            self.x1 = temp
        if self.y0 > self.y1:
            temp = self.y0
            self.y0 = self.y1
            self.y1 = temp


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


    def draw(self, t):
        t.penup()
        t.goto(self.x0, self.y0)
        t.pendown()

        for _ in range(2):
            t.forward(self.width())
            t.left(90)
            t.forward(self.height())
            t.left(90)
        t.penup()

    def info(self):
        """Print coordinates of the rectangle corners."""
        print(f"Lower left: ({self.x0}, {self.y0}), upper right: ({self.x1}, {self.y1})")



