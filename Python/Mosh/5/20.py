points = {"X": 1, "Y": 2}
points2 = dict(x=1, y=2)

points2["y"] = 20

print(points["Y"])

print(points.get("z", "NON"))

for key, val in points2.items():
    print(key, val)
