# Python program to demonstract Prime num range by (using while loop):

n = int(input('Enter a number : '))
i = 2
while (i < n) :
    j = 2
    while (j <= (i/j)) :
        if not (i%j) :
            break
        j = j+1
    if (j > i/j) :
        print(i)
    i = i+1
