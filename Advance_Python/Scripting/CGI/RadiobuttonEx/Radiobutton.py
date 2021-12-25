#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

import cgi, cgitb


form = cgi.FieldStorage()

if form.getvalue('subject'):
    subject = form.getvalue('subject')
else:
    subject = "NO Set"


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CheckBox</title>")
print("</head>")
print("<body>")
print("<h2>Selected Subject is : %s</h2>"%(subject))
print("</body>")
print("</html>")