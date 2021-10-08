# Python program to implement selection sort    without using min and max method

num = int(input("Enter a range : "))
list1 = [int(input("Enter an elements : "))for i in range(num)]

# for i in range(num):
#     data = int(input("Enter an element : "))
#     list1.append(data)

print("Unsorted List : ", list1)

for i in range(len(list1)-1):
    m_ind = i           # assume 1st number as min / max 
    for j in range(i+1, len(list1)):
        if list1[j] < list1[i]:         # compare with reset of numbers
            m_ind = j                   # after compare assign it to m_ind as min/max ele
    
    if list1[i] != list1[m_ind]:
       list1[i], list1[m_ind] = list1[m_ind], list1[i]
    
print("Sorted List : ",list1)