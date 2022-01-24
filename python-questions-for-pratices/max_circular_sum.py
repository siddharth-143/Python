# Python program for maximum contigous circle sum problem

# Standard Kadane's algorithm to find maximum subarray sum

def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending = 0
    for i in range(0, n):
        max_ending = max_ending + a[i]
        if max_ending < 0:
            max_ending = 0
        if max_so_far < max_ending:
            max_so_far = max_ending
    return max_so_far


# The function returns maximum circle contigous sum in a[]
def maxCircuralSum(a):
    n = len(a)

    # case 1 : get the maximum sum using standard kadanes algorithm
    max_kadane = kadane(a)

    # case 2 : now find the maximum sum that includes corner element
    max_wrap = 0
    
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]

    # max sum with corner element will be
    # array-sum - (-max subarray sum of inverted array)
    max_wrap = max_wrap + kadane(a)

    # The maximum circular sum will be maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

# Driver function to test above function
a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print("Maximum circular sum is : ", maxCircuralSum(a))
