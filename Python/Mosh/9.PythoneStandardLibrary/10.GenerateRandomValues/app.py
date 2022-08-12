import random
import string

print(random.random())
print(random.randint(1, 20))
print(random.choice([1.2, 6, 8, 10, 400, 5]))
print(random.choices([1.2, 6, 8, 10, 400, 5], k=4))
print(random.choices("abcdefghikjlmnopqrstuvwzxy", k=6))
print("".join(random.choices("abcdefghikjlmnopqrstuvwzxy", k=6)))

print("".join(random.choices(string.ascii_letters+string.digits, k=5)))

data = [1, 2, 3, 4, 5]

random.shuffle(data)
print(data)
