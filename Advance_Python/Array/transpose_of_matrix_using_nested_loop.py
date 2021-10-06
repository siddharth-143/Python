# Python program to demonstrate transpose a matrix using nested loop

x = [
    [12,3,4],
    [45,54,6],
    [7,8,9]
]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Iterate through rows
for i in range(len(x)) :
    # Iterate through columns
    for j in range(len(x[0])) :
        result[j][i] = x[i][j]

for r in result :
    print(r)