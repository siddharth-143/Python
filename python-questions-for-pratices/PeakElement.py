
def PeakElement(arr, n):
    res = 0
    if n==1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            res = arr[i]
    return res
arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print("Peak Element : ", PeakElement(arr, n))
