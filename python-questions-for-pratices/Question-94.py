"""
Question 94 :
    Write a program to solve a classic ancient chinese puzzle :
    We count 35 heads and 94 legs among the chickens and rabbits
    in a farm. HOw many rabbits and how many chickens do we have?

    Hints : Use for loop to iterate all possible solution.
"""

# Solution :

def solve(num_head, num_legs):
    no_slo = "No solution"
    for i in range(num_head + 1):
        j = num_head - 1
    if 2 * i + 4 * j == num_legs:
        return i, j
    return no_slo, no_slo


num_head = 2
num_legs = 8

solution = solve(num_head, num_legs)
print(solution)