import math

class Circle:
    def __init__(self, cx, cy, r, color="black", linewidth=2, segments=120):
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