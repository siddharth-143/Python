# Python program to implement Trapping rain water

def Find_Water(arr, n):

    res = 0
    for i in range(0, n):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
    return res

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
n = len(arr)
print("", Find_Water(arr, n))


# Time Complexity : O(n^2)
# Space Complexity : O(1)
