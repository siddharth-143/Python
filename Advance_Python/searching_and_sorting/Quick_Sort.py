# Python program to implement quick sort
# take first element as pivot


def pivot_place(list1, first, last):
    pivot = list1[first]
    left = first + 1			# first = 0 index of the list1
    right = last				# last = last index of the list1

    while True:
        while left <= right and list1[left] <= pivot:
            left += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[first], list1[right] = list1[right], list1[first]
    return right


# Divide rule
def Quick_Sort(list1, first, last):
    if first < last:
        p = pivot_place(list1, first, last)
        Quick_Sort(list1, first, p-1)
        Quick_Sort(list1, last, p+1)


num = int(input("Enter a range : "))
list1 = [int(input("Enter an elements : ")) for i in range(num)]
print("Unsorted list : ", list1)
Quick_Sort(list1, 0, len(list1)-1)
print("Sorted List : ", list1)