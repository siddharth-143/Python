class employee:
    def __init__(self):
        self.emp_name='siddharth'
        self.emp_id=100
        self.emp_salary=10000
    def show(self):
        print('emp_name :',self.emp_name)
        print('emp_id :',self.emp_id)
        print('emp_salary :',self.emp_salary)

e1=employee()
e1.show()
