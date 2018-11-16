from Converters import Converter

repeat = True
    
while repeat:
    try:
        num = input("Please enter a number: ")
        print(Converter(int(num)).convert())
    except(ValueError):
        print("Not a valid number.")
        repeat = False
