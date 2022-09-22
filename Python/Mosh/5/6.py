l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'dipu']

# //add
l1.append("dipu")
l1.insert(1, "moni")
print(l1)

# remove
l1.pop()
print(l1)
l1.pop(0)
print(l1)
l1.remove('dipu')

del l1[2:4]
print(l1)
l1.clear()
print(l1)
