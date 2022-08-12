class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def draw(self):
        return f"point {self.x} point {self.y}"


p = Point(10, 20)
a = Point(10, 20)


print(p == a)
print(p > a)
