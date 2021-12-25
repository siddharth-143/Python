#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

import cgi, cgitb

# instance of fieldStorage
form = cgi.FieldStorage()

# get data form field
if form.getvalue('maths'):
    math_flag = "ON"
else:
    math_flag = "OFF"

if form.getvalue('science'):
    science_flag = "ON"
else:
    science_flag = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CheckBox</title>")
print("</head>")
print("<body>")
print("<h2>CheckBox Math is : %s</h2>"%(math_flag))
print("<h2>CheckBox Science is : %s</h2>"%(science_flag))
print("</body>")
print("</html>")