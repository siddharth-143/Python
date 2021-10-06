 # Python program to demonstract factorial of num :

n = int(input('Enter a num : '))
fac = 1
if n < 0 :
    print('Sorry..!, factorial does not exist for negative num :')
elif n == 0 :
    print("The factorial of '0' is : 1")
else :
    for i in range(1, n+1):
        fac = fac*i
    print('The factorial of ', n, 'is : ',fac)
