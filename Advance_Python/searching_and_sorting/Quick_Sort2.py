# Python program to implement quick sort
# take last element as pivot and
# also random pivot and assign to last

import random


def pivot_place(list1, first, last):
    # this is for random pivot
    r_index = random.randint(first, last)
    list1[r_index], list1[last] = list1[last], list1[r_index]

    pivot = list1[last]
    left = first
    right = last - 1

    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[last], list1[left] = list1[left], list1[last]
    return left


def Quick_Sort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
        Quick_Sort(list1, first, p - 1)
        Quick_Sort(list1, last, p + 1)


list1 = [56, 26, 93, 17, 31, 44, 17]
# num = int(input("Enter a range : "))
# list1 = [int(input("Enter an elements : ")) for i in range(num)]
print("Unsorted list : ", list1)
Quick_Sort(list1, 0, len(list1) - 1)
print("Sorted List : ", list1)
