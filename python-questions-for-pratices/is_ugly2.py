def nth(n):
    ugly = [0]*n
    ugly[0] = 1

    i2=i3=i5 = 0
    num1 = 2
    num2 = 3
    num3 = 5

    for i in range(1, n):
        ugly[i] = min(num1, num2, num3)
        
        if ugly[i] == num1:
            i2 += 1
            num1 = ugly[i2] * 2
        if ugly[i] == num2:
            i3 += 1
            num2 = ugly[i3] * 3
        if ugly[i] == num3:
            i5 += 1
            num3 = ugly[i5] * 5
    return ugly[-1]

def main():
    n = 150
    print(nth(n))

if __name__=="__main__":
    main()
        
