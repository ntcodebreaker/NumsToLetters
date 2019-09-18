from Converters import Converter

repeat = True
    
while repeat:
    try:
        num = input("Please enter a number: ")
        print(Converter(int(num)).convert())
    except(ValueError):
        response = input("Not a valid number. Want to try again? ")
        repeat = response.lower() in ["y", "yes", "yep", "yeah"]
        