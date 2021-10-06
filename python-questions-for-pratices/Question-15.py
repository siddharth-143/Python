"""
Question 15 :
    Write a program that computes the values of a+aa+aaa+aaaa
    with a given digit as the value of a. Suppose the following
    input is supplied to the program : 9 Then, the output
    should be : 11106

    Hints : In case of input data begin supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

num = int(input("Enter a number : "))
n1 = int("%s" % num)
n2 = int("%s%s" % (num, num))
n3 = int("%s%s%s" % (num,num,num))
n4 = int("%s%s%s%s" % (num,num,num,num))
print(n1+n2+n3+n4)

"""
Output : 
    Enter a number : 9
    11106
"""