f = open("student.txt", mode="r")
# data1 = f.readline()        # read single line
# print(data1, end="")

data2 = f.readlines()       # read multiple lines
for i in data2:
    print(i, end="")
f.close()