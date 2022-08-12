class Point():
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"point {self.x} point {self.y}"


point = Point(10, 20)
another = Point(100, 200)

print(Point.default_color)
print(point.default_color)
print(another.default_color)
