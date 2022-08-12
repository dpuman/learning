l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1.sort()
print(l1)

print(sorted(l1, reverse=True))

items = [
    ("dipu", 1),
    ("cipu", 4),
    ("tipu", 2),
    ("bipu", 5),
]


def item_sort(item):
    return item[1]


items.sort(key=item_sort)

print(items)
