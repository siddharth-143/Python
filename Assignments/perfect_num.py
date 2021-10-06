 # Python program to demonstract perfect num :

n = int(input('Enter a number : '))
sum = 0
for i in range(1, n) :
    if (n % i == 0) :
        sum = sum + i
if (sum == n) :
    print('Perfect num ...')
else :
    print('Not perfect num...')
