class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        return f"point {self.x} point {self.y}"


p = Point.zero()
print(p.draw())
