items = [
    ("dipu", 1),
    ("cipu", 4),
    ("tipu", 2),
    ("bipu", 5),
]

new_items = [item[1] for item in items]
print(new_items)
new_items = [item for item in items if item[1] > 2]
print(new_items)
