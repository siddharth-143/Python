# Python program to implement direct index mapping allowed.

def search(X):
    if X >= 0:
        return has[X][0] == 1

    # if X is negative take the absolute of value X
    X = abs(X)
    return has[X][1] == 1


def insert(arr, n):
    for i in range(0, n):
        if arr[i] >= 0:
            has[arr[i]][0] = 1
        else:
            has[abs(arr[i])][1] = 1


if __name__ == "__main__":

    arr = [-1, 9, -5, -8, -5, -2]
    n = len(arr)
    MAX = 1000

    has = [[0 for i in range(2)] for j in range(MAX + 1)]
    insert(arr, n)

    X = -5

    if search(X) == True:
        print("Present")
    else:
        print("Not Present")
