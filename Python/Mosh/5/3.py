l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2, l3, *l4 = l1
l2, *l3, l4 = l1

print(l2, l3, l4)