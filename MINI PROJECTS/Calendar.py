"""
    Python program to print year of calendar
"""

import calendar

# Enter a year
yy = int(input("Enter year : "))

# Enter a month
mm = int(input("Enter month : "))

cal = calendar.TextCalendar(calendar.SUNDAY)

# year : 2021, column width : 2, lines per week : 1
# number of spaces between month columns ; 1
# no. of months per column : 3

# print whole year calendar
print(cal.formatyear(yy, 2, 1, 1, 3))

# print month and year
print(calendar.month(yy, mm))
