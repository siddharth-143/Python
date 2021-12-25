#!C:\Users\siddharth\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

from http import cookies

cook = cookies.SimpleCookie()
cook["username"] = "San"
cook["pass"] = "san@123"

cook["username"]["expires"] = "Sun, 29, Dec 2021 17:00:00 GMT"
cook["pass"]["expires"] = "Sun, 29, Dec 2021 17:00:00 GMT"

print(cook)
print("Content-type: text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>cook</title>")
print("</head>")

print("<body>")
print("<h3>cook Details</h3>")
print(cook["username"].value)
print(cook["pass"].value)
print("</body>")
print("<html>")