"""
Question 17 :
    Write a program that computes the net amount of a
    bank account based a transaction log from console input.
    The transaction log format is shown as following :
    D : 100 W : 200.

    D means deposit while W means withdrawal. Suppose the following input
    is supplied to the program : D : 300, D : 300, W : 200, D : 100 Then, the
    output should be : 500.

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

net_amount = 0
while True:
    choice = input("Enter a choice (like {D 100} or {W 100}): ")
    if not choice:
        break
    values = choice.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        net_amount += amount
    elif operation == "W":
        net_amount -= amount
    else:
        pass
print(net_amount)

"""
Output : 
    Enter a choice : D 300
    Enter a choice : D 300
    Enter a choice : W 200
    Enter a choice : D 100
    Enter a choice : 
    500
"""