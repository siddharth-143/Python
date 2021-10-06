from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
print(t.days)
# 4

print(t.seconds)
# 36000

#print(t.hours)
# AttributeError: 'datetime.timedelta' object has no attribute 'hours'

print(t.seconds / 60 / 60)
# 10.0

print(t.seconds / 3600)
# 10.0

eta = timedelta(hours=6)
today = datetime.today()
print(today)
# 2021-02-26 13:16:47.092251

print(today + eta)
# 2021-02-26 19:16:47.092251

print(str(today + eta))
# 2021-02-26 19:18:20.785789

"""
timedelta : 
    A duration of ime used for manipulating date
"""