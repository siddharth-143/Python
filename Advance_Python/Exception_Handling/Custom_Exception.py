# Custom Exception

class Error_In_Code(Exception):

    def __init__(self, data):
        self.data = data
    def __Str__(self):
        return repr(self.data)

try:
    raise Error_In_Code(2000)
except Error_In_Code as ae:
    print("Received error : ", ae.data)