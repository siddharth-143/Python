"""
Question 10 :
    Write a program that accepts a sequence of whitespace
    separated words as input and prints rhe words after removing
    all duplicate words and sorting them alphanumerically.
    Suppose the following input is supplied to the program:
    hello world and practice makes perfect and again hello world
    Then, the output should be : again hello world makes perfect practice
    world

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.We use set container
    to remove duplicated data automatically and then use sorted()
    to sort the data.
"""

# Solution :

sentence = input("Enter a sentence : ")
words = [word for word in sentence.split(" ")]
print(" ".join(sorted(list(set(words)))))

"""
Output : 
    Enter a sentence :   hello world and practice makes perfect and again hello world
    
    again and hello makes perfect practice world
"""