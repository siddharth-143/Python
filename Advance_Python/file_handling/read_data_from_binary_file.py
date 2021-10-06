
# Reading data from binary file :

import pickle
f2 = open('xyz.txt','rb')
k = pickle.load(f2)
print(k)
f2.close()
