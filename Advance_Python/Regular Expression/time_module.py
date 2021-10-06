# Python program to demonstract Time module

# 1. time() :
import time
seconds = time.time()
print('Seconds since epoch : ',seconds)

# 2. ctime() :
seconds = time.time()
local_time = time.ctime(seconds)
print('Local time : ', local_time)

# 3. time.sleep() : 
print('Hello siddhya')
time.sleep(2.4)
print('hii')

# 4. time.location() :
result = time.gmtime()
print('result :', result)
print('year :', result.tm_year)
print('tm_hour :', result.tm_hour)

# 5. gmtime() :
result = time.gmtime()
print('result : ', result)
print('year :', result.tm_year)
print('tm_hour :', result.tm_hour)

# [5]. OR
result = time.gmtime(123456789)
print('result : ', result)
print('year :', result.tm_year)
print('tm_hour :', result.tm_hour)

# 6. mktime() :
a = time.localtime()
b = time.asctime(a)
print(b)

# 7. asctime() :
a = time.localtime()
b = time.asctime(a)
print(b)

# 8. strftime() :
a = time.localtime
x = time.strftime('%m/%d/%y')
print(x)

# 9. time.dtrptime() :
x = '21 june,2021'
result = time.strptime(x, '%d %B,%Y')
print(result)























