# Reading data from file

f = open("student.txt", mode="r")
data1 = f.read(2)
data2 = f.read(2)
print(data1)
print(data2)
f.close()
print("complete!!!")