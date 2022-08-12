
class Animal:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print("EIGHTING")


class Dog(Animal):
    def walk(self):
        print("WALKING")


class Fish(Animal):
    def swim(self):
        print("SWIMMING")


f = Fish(10)

print(f.age)
f.eat()
f.swim()
