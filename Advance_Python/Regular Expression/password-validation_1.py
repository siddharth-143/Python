# Python program to demonstract password validaton by using regular expression :

import re
pas = input('Enter password :')
x = re.findall('(?=.*?[A-Z]) (?=.*?[a-z]) (?=.*?[0-9]) (?=.*?[!@#$%^&*()_+=<<?/.,\|{}[];:]).{8,}', pas)
if x :
    print('Valid password')

else :
    print('Invalid password')
