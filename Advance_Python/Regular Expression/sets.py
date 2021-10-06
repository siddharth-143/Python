# Sets

# 1.
import re

txt = 'The rain in Spain'
# Check if the string has any a, r, or n character :
x = re.findall('[arn]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 2.
txt = 'The rain in Spain'
# Check if the string has any character between a and n :
x = re.findall('[a-n]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 3.
txt = 'The rain in Spain'
# Check if the string has other character than a, r, or n :
x = re.findall('[^arn]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 4.
txt = 'The rain in Spain on 01-02-0123'
# Check if the string has any 0, 1, 2 or digit:
x = re.findall('[0123]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 5.
txt = 'Time is 12:15 PM'
# Check if the string has any digit :
x = re.findall('[0-9]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 6.
txt = 'Time is 12:15 PM'
# Check if the string has any two-digit number from 00 to 59 :
x = re.findall('[0-5][0-9]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 7.
txt = 'Time is 12:15 PM'
# Check if the string has any character from a to z lower case and A to Z upper case :
x = re.findall('[a-zA-Z]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')


# 8.
txt = 'Time is 12:15 PM +'
# Check if the string has any + character :
x = re.findall('[+]',txt)
print(x)
if x :
    print('Yes, there is atleast one match')
else :
    print('Not match')










    
