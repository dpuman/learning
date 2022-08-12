
class Animal(object):
    def __init__(self):
        self.age = 100

    def eat(self):
        print("EIGHTING")


class Mammal(Animal):

    def __init__(self):
        super().__init__()
        self.roll = 10

    def walk(self):
        print("WALKING")


class Fish(Animal):
    def swim(self):
        print("SWIMMING")


m = Mammal()
print(m.age)
print(m.roll)

print(isinstance(m, object))
print(isinstance(Mammal, object))
