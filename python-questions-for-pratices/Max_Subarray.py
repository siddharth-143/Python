# Python program to implement max subarray sum using kadane algorithm

def Max_Subarray(my_arr):
    current = 0
    max_sum = my_arr[0]

    for i in range(0, len(my_arr)):
        current = current + my_arr[i]
        if current < 0:
            current = 0
        elif max_sum < current:
            max_sum = current

    return max_sum


my_arr = [-2, -3, 4, -1, -2, 5, -3]
print("Maximum Sub-array Sum : ", Max_Subarray(my_arr))
