# Python program to implements selection sort using min and max method

list1 = [56, 3, 0, 78, 6, 0]       
print("Unsorted List : ", list1)


for i in range(len(list1)-1):           # -1 is for to avoid last iteration
    min_val = min(list1[i:])            # store min element  
    # max_val = max(list1[i;])            # store max element
    min_index = list1.index(min_val, i)            # count index and check for duplicate value
    
    if list1[i] != list1[min_index]:
        # swaping the number
        list1[i], list1[min_index] = list1[min_index], list1[i]
    
print("Sorted List : ", list1)
    