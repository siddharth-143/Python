def Maximum_Profit(arr, n):
    if n==1:
        return
    
    i = 0
    while (i < (n-1)):
        
        while ((i < (n-1)) and (arr[i+1] <= arr[i])):
            i += 1
            
        if (i == n-1):
            break
        buy = i
        i += 1

        while ((i < n) and (arr[i] >= arr[i - 1])):
            i += 1
               
        sell = i-1
        print("But on dat : ", buy, "\t", "Sell on day : ", sell)

arr = [100, 180, 260, 310, 40, 535, 695]
n = len(arr)
Maximum_Profit(arr, n)
