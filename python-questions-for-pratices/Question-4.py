"""
Question 4 :
    Write a program which accepts a sequence of comma-separated number
    from console and generate a list and tuple which contains every
    number.Suppose to the program : 1,2,3,4,5,6,7 Then, the output
    should be: ['1','2','3','4','5','6','7']

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.
    tuple() method can convert list to tuple
"""
# Solution :

values = input("Enter a number : ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)

"""
Output : 
    Enter a number : 1,2,3,4,5,6,7
    ['1', '2', '3', '4', '5', '6', '7']
    ('1', '2', '3', '4', '5', '6', '7')
"""