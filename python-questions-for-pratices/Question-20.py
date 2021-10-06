"""
Question 20 :
    Define a class with a generator which can iterate the
    numbers, which are divisible by 7, between a given range 0 and n.

    Hints : Consider user yield
"""

"""
yield expression : 
    Python yield returns a generator object. Generator are special
    functions that have to be iterated to get the values.
    Example :
        def test_yield():
            yield "Wel-come to siddhart-143 repository"
            s =  test_yield()
            print(s)
            
            Output : <generator object test_yield at 0x0000025159FF9580>
"""


# Solution :
n = int(input("Enter a range : "))
def num(n):
    i = 0
    while i < n:
        j = i
        i += 1
        if j % 7 == 0:
            yield j


for i in num(100):
    print(i, end=" ")

"""
Solution : 
    Enter a range : 100
    0 7 14 21 28 35 42 49 56 63 70 77 84 91 98  
"""