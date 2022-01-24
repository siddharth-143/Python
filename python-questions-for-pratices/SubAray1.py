# Python program to find subarray with given sum

def SubArray(a, n, sum_):
    curr_sum = a[0]
    start = 0

    i = 1
    while i <= n:
        while curr_sum > sum_ and start < i-1:
            curr_sum = curr_sum - a[start]
            start += 1
            
        if curr_sum == sum_:
            print("Sum found between indexes")
            print("%d and %d"%(start, i-1))
            return 1
        
        if i < n:
            curr_sum = curr_sum + a[i]
        i += 1
    print("No Subarrray found")
    return 0
a = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(a)
sum_ = 23
SubArray(a, n, sum_)


# Time Complexity : O(n)
# Space Complexity : O(1)
