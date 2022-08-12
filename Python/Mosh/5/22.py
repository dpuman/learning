from sys import getsizeof


t1 = (x for x in range(500))
print(t1)
print(getsizeof(t1))
