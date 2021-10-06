"""
     Python program to read height in in centimeter and then convert the height to inches and feet.
"""
cm = int(input("Enter the height in centimeters : "))
inches = 0.394 * cm
feet = 0.0328 * cm
print("The length in inches : ",round(inches, 2))
print("The length in feet : ",round(feet, 2))

"""
    The "round()" function returns a floating point number that is around version of
    the specified number, with the specified number of decimals
    
    The default number of decimal is 0,
    meaning that the function will return the nearest integer.
    
    Syntax :
        round(number, digits)
        
    number : Required. The number to be rounded
    digits : Optional. The number of decimals to use when rounding the number. Default is 0.
"""