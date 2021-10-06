# Python program to demonstract Url vslidation by using regular expression :

import re
url = input('enter the url :')
x = re.findall('^(https:\/\/www\.|http:\/\/\.|www\.)[a-zA-z0-9]+\.[a-z]{2,5}$',url)
if x :
    print('valid url')

else :
    print('invalid url')
