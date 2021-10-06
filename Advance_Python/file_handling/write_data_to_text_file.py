# write a data to text file

f = open('abc.txt','w')
f.write('Tata \n')
f.write('software \n')
f.write('solution \n')
print('data written to file successfully')

# write a list of data

list = ['aaa \n','bbb \n','ccc \n']
f.writelines(list)
print('list of lines written to the file successfully')

f.close()



# Data present in the file will be overridden everytime if we run the program.
# Instead of overrridding if we want append the operation then we should open the file as follows
# f = open('abc1','a')

