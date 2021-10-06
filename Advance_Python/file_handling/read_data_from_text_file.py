# Reading character data from text file


# 1. Read total data from file :

f = open('abc.txt', 'r')
data = f.read()
print(data)

# 2. To read only first 10 character :
data = f.read(10)
print(data)

# 3. To read data line by line :

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)

# 4. To read all lines into list :

lines = f.readlines()
for line in lines :
    print(line, end = '')
    
f.close()
