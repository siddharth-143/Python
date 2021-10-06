"""
Question 24 :
    Python has many build-in functions, and if you do not know
    how to use it, you can read document online or books. But Python
    has a build-in socument function for every build-in function.

    Write a program to print some Python build-in functions
    documents, suchas abs(), int(), input()
    And add document for your own function.

    HInts : The build-in document method is doc
"""

# Solution :

print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

num = int(input("Enter a number : "))


def square(num):
    """
        Return the square values of the input number.

        The input number must be integer.
    """
    return num ** 2


print(square(num))
print(square.__doc__)


"""
Output : 
    Return the absolute value of the argument.
    int([x]) -> integer
    int(x, base=10) -> integer
    
    Convert a number or string to an integer, or return 0 if no arguments
    are given.  If x is a number, return x.__int__().  For floating point
    numbers, this truncates towards zero.
    
    If x is not a number or if base is given, then x must be a string,
    bytes, or bytearray instance representing an integer literal in the
    given base.  The literal can be preceded by '+' or '-' and be surrounded
    by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
    Base 0 means to interpret the base from the string as an integer literal.
    >>> int('0b100', base=0)
    4
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
    Enter a number : 2
    4
    
            Return the square values of the input number.
    
            The input number must be integer.
        
    
    Process finished with exit code 0

"""