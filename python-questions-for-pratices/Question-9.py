""""
Question 9 :
    Write a program that accepts sequence of lines as input
    and print the lines after making all characters in the sentence
    capitalized.Suppose the following input supplied to the program :
    hello world practice makes perfect Then, output should be :
    HELLO WORLD PRACTICE MAKES PERFECT.

    Hints : In case of input data begin supplied to the
    question, it should be assumed to be a console input
"""

# Solution :

line = []
while True:
    sentence = input()
    if sentence:
        line.append(sentence.upper())
    else:
        break

for sentence in line:
    print(sentence)

"""
Output : 
    hello world practice makes perfect

    HELLO WORLD PRACTICE MAKES PERFECT
"""