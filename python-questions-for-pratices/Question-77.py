"""
Question 77 :
    Write a program to compress and decompress the string
    "hello world!hello world!hello world!hello world!"

    Hints : Use zlib.compress() ans zilb.decompress() to
    compress and decompress a string.
"""

# Solution :

import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))

"""
Output :
    b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
    b'hello world!hello world!hello world!hello world!'
"""


"""
zlib.compress(s) in python :
    With the help of zlib.compress(s) method, we can get compress the
    bytes of string by using zlib.compress(s) method

zlib.decompress(s) in python : 
    We can decompress the compressed bytes of string into original
    string by using : zlib.decompress(s) method
"""