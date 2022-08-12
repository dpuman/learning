from collections import deque

my_queue = [1, 2, 3]

my_queue = deque(my_queue)

my_queue.append(10)

my_queue.popleft()

print(my_queue)
