# file mode r+, w+, a+

# r+
# f = open("student.txt", mode="r+")
# print(f.tell())
# data = f.read()
# print(data)
# print(f.tell())
#
# f.write("Hello")
# print(f.tell())
# print(data)
# print(f.tell())
# f.close()

# w+

# f = open("student.txt", mode="w+")
# print(f.tell())
# f.write("Hello")
# print(f.tell())
#
# f.seek(0)
# data = f.read()
# print(data)
# print(f.tell())
# f.close()

# a+

f = open("student.txt", mode="a+")

print(f.tell())
f.write(" World")
print(f.tell())

f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)
print(f.tell())
f.close()