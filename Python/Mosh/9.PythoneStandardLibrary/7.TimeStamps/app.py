import time

print(time.time())


def send_email():
    for i in range(10000):
        pass


beg = time.time()
send_email()
end = time.time()
duration = end-beg

print(duration)
