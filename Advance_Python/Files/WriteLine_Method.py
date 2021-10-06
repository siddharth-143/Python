# Writing data to file using writeline method

f = open("student.txt", mode="w")
list = ["Karan\n", "Siddharth\n", "Ventya\n", "Rohit\n"]
f.writelines(list)
f.close()
print("Data write successfully")