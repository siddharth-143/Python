class A:
    def show(self):
        print('base class ')
class B(A):
    def show(self):
        super().show()
        print('child class')
b1=B()
b1.show()
