class A:
    def __init__(self):
        print('base class constructor ')

class B(A):
    def __init__(self):
        super().__init__()
        print('child class constructor ')

b1=B()
