"""
Question 88 :
    With a given list [12, 24,35, 24, 88,120, 155, 88, 120, 155],
    write a program to print this list after removing all duplicate values
    with original order reserved.

    Hints : Use set() to store a number of values without duplicate.
"""

# Solution :


def remove_duplicate(li):
    new_list = []
    set_list = set()

    for i in li:
        if i not in set_list:
            set_list.add(i)
            new_list.append(i)

    return new_list

li = [12, 24,35, 24, 88,120, 155, 88, 120, 155]
print(remove_duplicate(li))

"""
Output :
    [12, 24, 35, 88, 120, 155]
"""