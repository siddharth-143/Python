# Python program to find minimum number of platforms required
# on a railway station

def Find_Platform(arr, dep, n):

    arr.sort()
    dep.sort()
    
    result = 1
    plat = 1
    i = 1
    j = 0
    
    while(i < n and j<n):
        
        if arr[i] <= dep[j]:
            plat += 1
            i += 1
            
        elif arr[i] >= dep[j]:
            plat -= 1
            j += 1
            
        if plat > result:
            result = plat
            
    return result

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print("Minimum Number of platform required : ", Find_Platform(arr, dep, n))


# Time Complexity : O(N log N)
# Space Complexity : O(1)
