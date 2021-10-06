# Python program to demonstrate multiplication of matrix :
A = []
n = int(input('Enter a n for n x n matrix : '))
print('Enter the elements ::> ')
for i in range(n):
    # temporary list to store the row
    row = []
    for j in range(n):
        # add a input to row list
        row.append(int(input()))
        # add a rew to the list
        A.append(row)
print(A)