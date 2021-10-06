"""
Question 13 :
    Write a program that accepts a sentence and calculate the
    number of the letters and digits. Suppose the following input is
    supplied to the program : hello world! 123 Then, the output should
    be : LETTER 10 DIGIT 3.

    Hints : In case of input data being supplied to the question, it
    should be assumed to be a console input.
"""

# Solution :

sentence = input("Enter a string including number : ")
dic = {"DIGITS" : 0, "LETTERS" : 0}
for i in sentence:
    if i.isdigit():
        dic["DIGITS"] += 1
    elif i.isalpha():
        dic["LETTERS"] += 1
    else:
        pass
print("LETTERS : ", dic["LETTERS"])
print("DIGITS : ", dic["DIGITS"])

"""
Output :
     Enter a string including number :  HELLO WORLD! 123
     LETTERS :  10
     DIGITS :  3
"""