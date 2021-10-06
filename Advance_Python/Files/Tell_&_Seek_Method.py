# tell and seek method

f = open("student.txt", mode="r")

# print(f.tell())
# data1 = f.read(5)
# print(data1)
# print(f.tell())
#
# data2 = f.read(5)
# print(data2)
# print(f.tell())

print(f.tell())
f.seek(7)
print(f.tell())
data1 = f.read()
print(data1)

f.seek(2)
print(f.tell())
data2 = f.read()
print(data2)