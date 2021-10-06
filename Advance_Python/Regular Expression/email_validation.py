# Python program to implements Email validation  by using Regular expression

import re
email = input('Enter the email :')
x = re.findall('^[a-z][A-z][a-zA-z0-9]*@gmail.com', email)
if x :
    print('Valid email id')

else :
    print('Invalid email')
