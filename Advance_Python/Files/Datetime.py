# datetime

from datetime import datetime, timedelta

dt1 = datetime(year=2021, month=8, day=19)
dt1 = datetime(year=2021, month=9, day=29, hour=12, minute=34)
dt3 = datetime(2012, 3, 31)
dt4 = datetime(2019, 2, 21, 3, 23)
print(dt1.year)

dt5 = datetime.now()
print(dt5)

dt6 = datetime.today()
print(dt6)

# timedelta
dt7 = timedelta(days=10)
d = datetime.today()
print(dt7 + d)

# compare two date
d1 = datetime(2019, 12, 30)
d2 = datetime(210, 12, 30)
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)
print(d1 != d2)


# Formatting date and time
dt = datetime.today()

new = dt.strftime("%B, %d, %Y")
print(new)
print()

new1 = dt.strftime("%d/%b/%Y")
print(new1)
print()

new2 = dt.strftime("%d-%m-%Y")
print(new2)
print()

new3 = dt.strftime("%H:%M:%S")
print(new3)
print()

new4 = dt.strftime("%I:%M:%S")
print(new4)
print()