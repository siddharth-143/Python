# Python program to read from standard input

import sys

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print("Input Line")
print("Done")
