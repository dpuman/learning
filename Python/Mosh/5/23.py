first = [1, 2, 3, 4]
second = [5, 6, 7, 8, 9]

third = [*first, *"dipu", *second]
print(third)


d1 = {"X": 1}
d2 = {"y": 20}

d3 = {**d1, **dict(z=5), **d2}
print(d3)
