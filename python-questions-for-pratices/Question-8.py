"""
Question 8 :
    Write a program that accepts a comma separated sequence
    of the words as input and prints the words as input and
    print the words in a comma-separated sequence after sorting
    them alphabetically.Suppose the following input is supplied
    to the program: without,hello,bag,world. Then, the output
    should be bag,hello,without,world

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

name = input("Enter a words : ")
items = [x for x in name.split(",")]
items.sort()
print(",".join(items))

"""
Output : 
    Enter a words : without, hello, bag, world
    bag, hello, world,without
"""