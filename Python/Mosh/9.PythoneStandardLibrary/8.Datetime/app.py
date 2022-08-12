from datetime import datetime
import time

dt = datetime(2018, 1, 1)
print(dt)
dt = datetime.now()
print(dt)
dt = datetime.strptime("2018/01/05", "%Y/%m/%d")
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

print(dt2 > dt1)
