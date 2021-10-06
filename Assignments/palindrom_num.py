 # Python program to demonstract palindrom num :

n = int(input('Enter a num : '))
temp = n
rev = 0
while (n > 0):
    dig = n%10
    rev = rev*10+dig
    n = n// 10
if (temp == rev) :
    print('The num is a palindrome....')
else :
    print("The num isn't a palindrom...")
