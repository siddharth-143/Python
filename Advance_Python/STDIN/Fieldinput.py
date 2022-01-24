# Python program to read standard input using fileinput module

import fileinput

for fileinput_line in fileinput.input():
    if 'Exit' == fileinput_line.rstrip():
        break
print("Done")
