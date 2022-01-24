# Python program to find subarray with given sum

def Sub_Array(a, n, sum_):
    for i in range(n):
        curr_sum = a[i]
        
        j = i+1
        while j <= n:
            
            if curr_sum == sum_:
                print("Sum found between")
                print("Indexs %d and %d "%(i, j-1))
                return 1
            if curr_sum > sum_ or j == n:
                break
            
            curr_sum = curr_sum + a[j]
            j += 1
            
    print("No Subarray found")
    return 0
            
a = [1, 2, 3]
n = len(a)
sum_ = 2
Sub_Array(a, n, sum_)


# Time Complexity : O(n^2)
# Space Complexity : O(1)
