class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return f"point {self.x} point {self.y}"


point = Point(10, 20)

print(point.draw())
