# Regular Expression

# Function on Regular expression

# 1. findall()

import re
s1 = "This is python programming"

x = re.findall('is :',s1)
print(x)

# 2. split()

x = re.split('\s',s1)
print(x)

# 3. sub()

x = re.sub('\s','9',s1)
print(x)

x = re.sub('\s','9',s1,2)
print(x)

# 4. match()

s = input('Enter pattern to check :')
x = re.match(s,'abcdefgh')

if x!= None :
    print('Mathch is available at the beginning of the dteing')
    print('Start index :',x.start(),' and End index :',x.end())

else :
    print('Match is not available at the beginning of the string')


# 5. fullmatch() :

s = input('Enter pattern to check :')
x = re.fullmatch(s,'hello')

if x!= None :
    print('Full string match ')

else :
    print('Full string not match')


# search() :

s1 = "This is python programming"

x = re.search('This',s1)
print(x)

x = re.search('python',s1)
print(x)

# string------------------->>>>>>>>>>>>>methods
x = re.search('python',s1)
print(x.string)

# group ------------------------>>>>>>>>>>> methods
x = re.search('python',s1)
print(x.group())
