def Maximum_Profit(arr, days):
    profit = 0

    for i in range(days):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

arr = [100, 180, 260, 310, 40, 535, 695]
print("Maximum Profit : ", Maximum_Profit(arr, len(arr)))
