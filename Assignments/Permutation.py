# Python program to print all permutations using library function

from itertools import permutations

prem = permutations([1,2,3])

for i in list(prem):
	print(i)