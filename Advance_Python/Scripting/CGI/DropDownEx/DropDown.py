#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('dropdown'):
    subject = form.getvalue('dropdown')
else:
    subject = "Not Entered"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CheckBox</title>")
print("</head>")
print("<body>")
print("<h2>Selected Subject is : %s</h2>"%(subject))
print("</body>")
print("</html>")