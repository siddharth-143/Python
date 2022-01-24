# Python program to find equilibrium index of an array

def Eqiulibrium(arr):
    n = len(arr)
    rightsum = 0
    leftsum = 0

    for i in range(n):
        leftsum = 0
        rightsum = 0
        
        for j in range(i):
            leftsum += arr[j]
            
        for j in range(i+1, n):
            rightsum += arr[j]
        if leftsum == rightsum:
            return i
        
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print("Equilibrium index of an array : ", Eqiulibrium(arr))

# Time Complexity : O(n^2)
