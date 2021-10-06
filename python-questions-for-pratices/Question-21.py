"""
Question 21 :
    A robot moves in a plane starting from the origin point (0,0).
    The robot can moves toward UP, DOWN, LEFT, RIGHT with a given
    steps. The trace of robot movement is shown as the following :
    UP 5 DOWN 3 LEFT 3 RIGHT 2. The numbers after the direction are
    steps. Write a program to compute the distance from current position
    after a sequence of movements and original point. If the distance is a
    float, then just print the nearest integer. Example : If the following
    tuples are given as input to the program : UP 2 DOWN 3 LEFT 3 RIGHT 2
    Then, the output of the program should be : 2

    HInts : In case of input data being supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

import math
position = [0, 0]
while True:
    num = input("Enter a steps : ")
    if not num:
        break

    movement = num.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        position[0] += steps

    elif direction == "DOWN":
        position[0] -= steps

    elif direction == "LEFT":
        position[1] -= steps

    elif direction == "RIGHT":
        position[1] += steps

    else:
        pass

print(int(round(math.sqrt(position[1]**2 + position[0]**2))))


"""
Output : 
    Enter a steps : UP 5
    Enter a steps : DOWN 3
    Enter a steps : LEFT 3
    Enter a steps : RIGHT 2
    Enter a steps : 
    2
"""