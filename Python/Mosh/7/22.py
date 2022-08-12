from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a = Point(10, 20)
b = Point(10, 20)

print(a == b)

# If using only data in a class use named tuple

Point = namedtuple("Point", ["x", "y"])

c = Point(x=10, y=20)
d = Point(x=10, y=20)

print(c == d)
