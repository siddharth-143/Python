
# Python program to demonstract exception handling
# User exception handling

class bank_error(Exception) :
    def __init__(self,ms) :
        self.dem= ms
        
amount = int(input('Enter the amount to withdrawal :'))
stored_amount = int(input('Enter the stored amount in bank :'))

try :
    if stored_amount<=2000 :
        raise bal_error('Insufficient balance...!')
    else :
        print('Your withdrawal amount : ',amount)

except bank_error as msg :
    print(msg)

except bal_error as dem :
    print(dem)
