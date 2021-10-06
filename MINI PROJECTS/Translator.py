"""
    Python program to implement translator
"""
from translate import Translator
translator = Translator(from_lang=input("Enter your source language : "), to_lang=input('Enter you destination language : '))
translation = translator.translate(input("Enter you text : "))
print(translation)

# Output :
"""
    Enter your source language : en
    Enter you destination language : hi
    Enter you text : i am siddharth
    मैं सिद्धार्थ हूं
"""
