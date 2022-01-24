# Python program to find minimum number of platforms required
# on a railway station


def FindPlatform(arr, dep, n):

    times = []
    for i in range(n):
        times.append([arr[i], 'a'])
        times.append([dep[i], 'd'])

    times = sorted(times, key=lambda x: x[1])
    times = sorted(times, key=lambda x: x[0])

    result, plat = 0, 0

    for i in range(2*n):
        if times[i][1] == 'a':
            plat += 1
            result = max(plat, result)
        else:
            plat -= 1
    return result

arr = [ 900, 940, 950, 1100, 1500, 1800 ]
dep = [ 910, 1200, 1120, 1130, 1900, 2000 ]
n = len(arr)
print("Minimum number of platform required : ", FindPlatform(arr, dep, n))
