 # Python program to ask the user for a range and display all Armstrong num in that interval :

lower = int(input('Enter a lower range : '))
upper = int(input('Enter a upper range : '))

for num in range(lower,upper + 1) :
    # Initialize sum
    sum = 0

    # Find the sum of the cube of each digit
    temp = num
    while temp > 0 :
        digit = temp % 10
        sum += digit**3
        temp //= 10

    if num == sum :
        print(num)
