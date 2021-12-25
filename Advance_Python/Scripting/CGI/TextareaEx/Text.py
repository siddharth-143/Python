#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

import cgi, cgitb

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "Not Entred.."

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>CheckBox</title>")
print("</head>")
print("<body>")
print("<h2>Entered Text Content is : %s</h2>"%(text_content))
print("</body>")
print("</html>")