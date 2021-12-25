#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

import cgi, cgitb

form = cgi.FieldStorage()

# get data
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title> Get-Method</title>")
print("</head>")
print("<body>")
print("<h2>Hello %s %s</h2>"%(first_name, last_name))
print("</body>")
print("</html>")