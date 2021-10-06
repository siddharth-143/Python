"""
Question 43 :
    Write a program which accepts a string as input to print
    "YES" if the string is "yes" or "Yes", otherwise print "No".:type

    Hints : Use if statement to judge condition.
"""

# Solution :

name = input("Enter a name : ")
if name == "YES" or name == "Yes" or name == "yes":
    print("Yes")

else:
    print("No")

"""
Output : 
    Enter a name : yes
    Yes
    
    Process finished with exit code 0
"""