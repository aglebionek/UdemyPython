import datetime

mytime = datetime.time(2, 20)
print(mytime.hour, mytime.minute, mytime)

anothertime = datetime.time(13,20,1,20)
print(anothertime) # from larger unit to smaller
print(type(anothertime))

today = datetime.date.today()
print(today.year, today.month, today.day, today)
print(today.ctime())

dt = datetime.datetime(2021, 8, 3, 14, 20, 1)
print(dt)
dt = dt.replace(year=2020)
print(dt)

date1 = datetime.date(2021, 9, 20)
date2 = datetime.date(2020, 9, 12)
print(date1 - date2)

datetime1 = datetime.datetime(2021, 11, 3, 22, 00, )
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)
diff = datetime1 - datetime2
print(diff, diff.seconds, diff.total_seconds())