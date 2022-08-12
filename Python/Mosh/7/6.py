class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"point {self.x} point {self.y}"

    def draw(self):
        return f"point {self.x} point {self.y}"


p = Point(10, 20)
print(p)
