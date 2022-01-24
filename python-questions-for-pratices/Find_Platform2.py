# Python program to find minimum number of platform
# required on a railway station

def Platform(arrival, departure, n):

    platform = [0]*2631
    required = 1

    for i in range(n):
        platform[arrival[i]] += 1
        platform[departure[i]+1] -= 1

    for i in range(1, 2631):
        platform[i] = platform[i] + platform[i-1]
        required = max(required, platform[i])
    return required

arr = [ 900, 940, 950, 1100, 1500, 1800 ]
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]
n = len(arr)
print("Minimum number of platform required : ", Platform(arr, dep, n))
