import math


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        number_one = (x2 - x1) ** 2
        number_two = (y2 - y1) ** 2
        return math.sqrt((number_one + number_two))

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

line = Line(coordinate1, coordinate2)

print(line.distance())

print(line.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)


c = Cylinder(2, 3)

print(c.volume())

print(c.surface_area())
