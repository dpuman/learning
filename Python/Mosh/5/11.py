items = [
    ("dipu", 1),
    ("cipu", 4),
    ("tipu", 2),
    ("bipu", 5),
]

new_list = list(filter(lambda x: x[1] > 2, items))
print(new_list)
