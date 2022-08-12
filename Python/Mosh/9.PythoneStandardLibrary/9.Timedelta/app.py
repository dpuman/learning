from datetime import datetime, timedelta

dt = datetime(2018, 1, 5)
dt2 = datetime.now()

duration = dt2-dt

print(duration)
print(duration.days)
print(duration.seconds)
print(duration.total_seconds())

dt = datetime(2018, 1, 5)+timedelta(days=1, seconds=30)
print("hola", dt)
