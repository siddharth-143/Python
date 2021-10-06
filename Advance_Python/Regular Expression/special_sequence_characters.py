# special sequence characters :

# 1.
import re
txt = 'The rain in Spain '
# Check if the string starts with 'The' :
x = re.findall('\AThe', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

    
# 2[a].
txt = 'The rain in Spain '
# Check if 'ain' is present at the beginning of a WORD :
x = re.findall(r'\bain', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')


# 2[b].
txt = 'The rain in Spain '
# Check if 'ain' is present at the end of a WORD :
x = re.findall(r'ain\b', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 3[a].
txt = 'The rain in Spain '
# Check if 'ain' is present, but NOT at the beginning of a word :
x = re.findall(r'\Bain', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 3[b].
txt = 'The rain in Spain '
# Check if 'ain' is present, but NOT at the end of a word :
x = re.findall(r'ain\B', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 4[a].
txt = 'The rain in Spain '
# Check if the string contains any digit (number fron 0-9) :
x = re.findall('\d', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 4[b].
txt = 'The rain in 1 S2pain '
# Check if the string contains any digit (number fron 0-9) :
x = re.findall('\d', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 5.
txt = 'Hello123'
# Return a match at no-digit character :
x = re.findall('\D',txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 6.
txt = 'The rain in 1 S2pain '
# Return a match at every white-space character :
x = re.findall('\s', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 7.
txt = 'Hello world'
# Return a match at every NON white-space character :
x = re.findall('\S', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 8.
txt = 'This is account_no 1234'
# Return a match at evey word character (characters from a to z , digits from 0-9, and the underscore_character):
x = re.findall('\w', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')


# 9.
txt = 'This is account_no 1234!#'
# Return a match at evey NON word character (characters NOT between a and z. Like '!','?',whitespace etc):
x = re.findall('\W', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')

# 10.
txt = 'The rain in spain'
# Check if the string end with 'Spain' :
x = re.findall('spain\Z', txt)
print(x)
if x :
    print('Yes, there is a match')
else :
    print('No match')









    
