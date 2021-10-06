# Directory

import os

print(os.getcwd())      # current working directory
# os.mkdir()      # create a directory / folder
# os.makedirs()       # create multiple directory within directory
# os.chdir()      # change directory
# os.rename()     # rename the directory
# os.rmdir()      # delete specific directory
# os.removedirs()     # delete multiple directory

w = os.walk(".", topdown=False)                 # by default topdown = True
for i in w:
    print(i)