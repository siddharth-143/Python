# Python program to find the equilibrium index of an array

def Equilibrium(arr):
    leftsum = 0
    total = sum(arr)

    for i, num in enumerate(arr):
        total -= num

        if leftsum == total:
            return i
        leftsum += num
    return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
print("Equilibrium index of an array : ", Equilibrium(arr))

# Time Complexity : O(n)
