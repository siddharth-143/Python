"""
Question 80 :
    Write a program to generated all sentence where subject
    is in ["i", "you"] and verbs is in ["play", "love"] and the
    object is in ["hockey", " football"].

    Hints : Use list[index] notation to get a elements from a list..
"""

# Solution :

subject = ["I", "You"]
verbs = ["Play", "Love"]
object = ["Hockey", "Football"]

for i in range(len(subject)):
    for j in range(len(verbs)):
        for k in range(len(object)):
            sentence = "%s %s %s." % (subject[i], verbs[j], object[k])

    print(sentence)

"""
Output : 
    I Love Football.
    You Love Football.
"""