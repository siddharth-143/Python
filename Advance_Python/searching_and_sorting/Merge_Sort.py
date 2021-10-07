# Python program to implement merge sort

def MergeSort(list1):
    if len(list1) > 1:
        mid = len(list1)//2         # divided the list1
        left_list = list1[:mid]      # store from starting to less than mid
        right_list = list1[mid:]     # store from mid to length of list1
        MergeSort(left_list)
        MergeSort(right_list)
        i = 0       # index of left_list
        j = 0       # index of right_list
        k = 0       # store ele in list1
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            list1[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list1[k] = right_list[j]
            j += 1
            k += 1


num = int(input("How many elements do you want in list : "))
list1 = [int(input()) for i in range(num)]
MergeSort(list1)
print("Sorted List : ", list1)