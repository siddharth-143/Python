from datetime import date
from datetime import datetime

print(datetime.today())
# 2021-02-25 19:40:36.445132

today = datetime.today()
print(today)
# 2021-02-25 19:40:36.445132

print(type(today))
# <class 'datetime.datetime'>

today_date = date.today()
print(today_date)
# 2021-02-25

print(type(today_date))
# <class 'datetime.date'>

print(today_date.month)
# 2

print(today_date.year)
# 2021

print(today_date.day)
# 25

print(today_date.weekday())
# 3

print(today_date.isoweekday())
# 4

print(today_date.isocalendar())
# datetime.IsoCalendarDate(year=2021, week=8, weekday=4)

print(today_date.timetuple())
# time.struct_time(tm_year=2021, tm_mon=2, tm_mday=25, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=56, tm_isdst=-1)

christmas = date(today_date.year, 12, 25)
print(christmas)
# 2021-12-25

if christmas != today_date:
    print("Sorry there are till " + str((christmas - today_date).days) + " until Christmax")

else:
    print("Yay it's christmas")
# Sorry there are till 303 until Christmax