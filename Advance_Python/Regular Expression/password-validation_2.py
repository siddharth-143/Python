# Python program to demonstract password validation by using regular expression :

import re
flag = 0
pas = input('Enter a password :')

x = re.search('[a-z]', pas)
y = re.search('[A-Z]', pas)
z = re.search('[0-9]', pas)
q = re.search('[!@#$%]', pas)
if not x :
    flag = 1
if not y :
    flag = 1
if not z :
    flag = 1
if not q :
    flag = 1
if len(pas)<8 :
    flag =  1
if (flag==0) :
    print('Valid password')
else :
    print('Invalid password')
