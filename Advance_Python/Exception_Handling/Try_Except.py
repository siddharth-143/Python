# Try Except block

try:
    f = open("file.txt", "r")
except FileNotFoundError:
    print("No such file or directory")
else:
    print("File Open Successfully")
