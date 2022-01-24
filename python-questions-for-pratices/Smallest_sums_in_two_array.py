# Python program to find k pairs with smallest sums in two
# arrays

import sys

def Smallest_pair(arr1, arr2, n1, n2, k):
    if k > n1*n2:
        print("k pair don't exist")
        return
    index = [0 for i in range(n1)]

    while k>0:
        min_sum = sys.maxsize
        min_index = 0

        for i in range(0, n1, 1):
            if index[i] < n2 and arr1[i] + arr2[index[i]] < min_sum:
                min_index = i
                min_sum = arr1[i] + arr2[index[i]]
        print(arr1[min_index], ",", arr2[index[min_index]], ",", end=" ")
        index[min_index] += 1
        k -= 1


arr1 = [1, 7, 11]
arr2 = [2, 4, 6]
n1 = len(arr1)
n2 = len(arr2)
k = 3
ans = Smallest_pair(arr1, arr2, k, n1, n2)
print(ans)
