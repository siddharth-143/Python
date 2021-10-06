 # Python program to demonstract bubble sort by using list[] :

a = []
n = int(input('Enter the total num of elements : '))
for i in range(n) :
    val = int(input('Enter the elements %d list of elements : '))
    a.append(val)

for i in range(n - 1) :
    for j in range (n - i - 1) :
        if (a[j] > a[j + 1]) :
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print('The sorted list : ', a)
