# Python program for zig-zag conversion of array

def Zig_Zag(arr, n):
    
    # flag ture indicates relation "<" is expected,
    # else ">" is expected. The first expected relation
    # is "<"
    flag = True
    for i in range(n-1):
        # "<" relation expected
        if flag is True:

            # if we have a situation like A > B > C,
            # we get A > B < C
            # swapping B and C
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            # ">" relation expected
                
        else:

            # if we have a situation like A > B > C,
            # we get A < C > B
            # by swapping B and C
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
        flag = bool(1-flag)
    print(arr)


arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
Zig_Zag(arr, n)
