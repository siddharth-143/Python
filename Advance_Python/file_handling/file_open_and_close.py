# file handing
# open and close file (basic demo)

f = open('abc.txt','w')
print('File name :',f.name)
print('File mode :',f.mode)
print('Is file readable :',f.readable())
print('Is file writeable :',f.writable())
print('Is file close :',f.close())
f.close()
print('Is file close :',f.close)
