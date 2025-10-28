import random
from src.main.del2.drawing import Rectangle


def createRectangle(xMin, yMin, xMax, yMax):
    random_list = []
    for i in range(2):
        random_list.append(random.randint(xMin, xMax))
        random_list.append(random.randint(yMin, yMax))

    rectangle = Rectangle(random_list[0], random_list[1], random_list[2], random_list[3])
    rectangle.control_corners()
    return rectangle


if __name__ == "__main__":
    rectangles = []
    for i in range(3):
        rectangles.append(createRectangle(0, 0, 100, 100))

    for r in rectangles:
        r.info()
