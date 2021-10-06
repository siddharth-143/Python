# Metacharacters

# 1.
import re
txt = 'The rain in Spain'

# Find all lowerr case characters alphabeticall between 'a' and 'm' :
x = re.findall('[a-m]',txt)
print(x)

# 2.
txt = 'That will be 59 dollars'

# Find all digit characters :
x = re.findall('\d', txt)
print(x)

# 3.
txt = 'hello world'

# Search for a sequence that start with 'he' , followed by two (any) characters, snd an 'o' :
x = re.findall('he..o',txt)
print(x)

# 4.
txt = 'hello world'
# Check if the string with 'hello' :

x = re.findall('hello',txt)
if x :
    print("Yes, the string with 'hello'")
else :
    print('No match')

# 5.
txt = 'hello world'
# Check if the string with 'world' :

x = re.findall('world$',txt)
if x :
    print("Yes, the string with 'world'")
else :
    print('No match')

# 6.
txt = 'Friend in need is a friend in deed'
x = re.findall('ee*',txt)
print(x)

# 7.
txt = 'Friend in need is a friend in deed'
x = re.findall('ee+',txt)
print(x)

# 8.
txt = 'Friend in need is a friend in deed'
x = re.findall('e{2}',txt)
print(x)


# 9.
txt = 'The rain in spain falls mainly in the palin! '

# Check if the string contains 'a' followed by excatly two 'l' characters :
x = re.findall('al{2}',txt)
print(x)

# 10.
txt = 'The rain in spain falls mainly in the palin! '

# Check if the string contains either 'falls' or 'stays':
x = re.findall('falls | stays',txt)
print(x)

























