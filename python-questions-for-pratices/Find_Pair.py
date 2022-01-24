# Python programt to fing a pair with the given difference

def Find_pair(arr, n):
    
    size = len(arr)

    # initialize position of two elements
    i, j = 0, 1

    # search for a pair
    while i < size and j < size:
        if i != j and arr[j] - arr[i]==n:
            print("found pair (", arr[i],",", arr[j],")")
            return True
        
        elif arr[j]-arr[i] < n:
            j += 1
            
        else:
            i += 1
    print("Not found pair")
    return False


arr = [1, 8, 30, 40, 100]
n = 60
Find_pair(arr, n)

# Time complexity : O(n log(n))
