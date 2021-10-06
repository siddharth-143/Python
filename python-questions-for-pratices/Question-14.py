"""
Question 14 :
    Write a program that accepts a sentence and calculate the
    number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program :
    Hello world! Then, the output should be :
    UPPER CASE : 1 LOWER CASE : 0.

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

sentence = input("Enter a string : ")
dic = {"UPPER CASE " : 0, "LOWER CASE" : 0}
for i in sentence:
    if i.isupper():
        dic["UPPER CASE "] += 1
    elif i.islower():
        dic["LOWER CASE"] += 1
    else:
        pass

print("UPPER CASE : ", dic["UPPER CASE "])
print("LOWER CASE : ", dic["LOWER CASE"])

"""
Output : 
    Enter a string : Hello world!
    UPPER CASE :  1
    LOWER CASE :  9
"""