
# Write data to binary files :

import pickle
f1 = open('xyz.txt','wb')
pickle.dump('Hello world',f1)

l1 = ['mini',15]
pickle.dump(l1,f1)
print('Data write successfully')
f1.close()


# Reading data from binary file :

f2 = open('xyz.txt','rb')
k = pickle.load(f2)
print(k)
f2.close()
