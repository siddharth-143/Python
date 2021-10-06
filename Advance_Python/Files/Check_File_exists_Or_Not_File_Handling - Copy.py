# Check file exists or not File Handling

import os
if os.path.isfile("Student.txt"):
    f = open("student.txt")
    print("File Opened")
    f.close()
else:
    print("File Not Found")