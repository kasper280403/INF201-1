import random
import turtle

from src.main.del2.drawing import Rectangle


def create_rectangle(xMin, yMin, xMax, yMax):

    random_list = []
    for i in range(2):
        random_list.append(random.randint(xMin, xMax))
        random_list.append(random.randint(yMin, yMax))

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3])
    rectangle.control_corners()
    return rectangle

def create_turtle():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('green')
    t.speed(0)

    return t


if __name__ == "__main__":
    rectangles = []
    for i in range(3):
        rectangles.append(create_rectangle(-300, -300, 300, 300))

    for r in rectangles:
        r.info()

    t = create_turtle()

    for r in rectangles:
        r.draw(t)

    turtle.done()


