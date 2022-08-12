class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def draw(self):
        return f"point {self.x} point {self.y}"


p = Point(10, 20)
a = Point(10, 20)

combine = p+a
difference = p-a

print(combine.x, combine.y)
print(difference.x, difference.y)
