# Python program to solve chocolate distribution problem

def Find_Min(arr, n, m):

    # if there are no chocolates or number of student is 0
    if n==0 or m==0:
        return 0

    # sort the given packets
    arr.sort()

    # number of student cannot be more than number of packets
    if n < m:
        return -1

    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]
    
    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i+m-1]-arr[i])

    return min_diff


if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,30, 40, 28, 42, 30, 44, 48, 43, 50]
    n = len(arr)
    m = 7
    print("Minimum difference is : ", Find_Min(arr, n, m))
