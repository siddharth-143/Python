"""
Question 19 :
    You are required to write a program to sort the (name, age, height)
    tuple by ascending order where name is string, age and height are
    numbers. The tuple are input by console. The sort criteria is
    1 : Sort based on name; 2 : Then sort based on age;
    3 : Then sort by score. The priority is that name->age->score.
    If the following tuples are given as input to the program:
    Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then,
    the output of the program should be : [('Jonh', '20', '90'),
    ('Jony', '17', '91'),('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '60')]

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.  We use itemgetter
    to enable multiple sort keys.
"""

# Solution : from operator import itemgetter, attrgetter

from operator import *

# OR

# from operator import itemgetter, attrgetter

l = []
while True:
    sen = input("Enter a name age and score : ")
    if not sen:
        break
    l.append(tuple(sen.split(",")))

print(sorted(l, key=itemgetter(0, 1, 2)))

"""
Output : 
    Enter a name age and score : Tom,19,80
    Enter a name age and score : John,20,90
    Enter a name age and score : Jony,17,91
    Enter a name age and score : Jony,17,93
    Enter a name age and score : Json,21,85
    Enter a name age and score : 
    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""
