from Converters import Converter

if __name__ == '__main__':
    repeat = 'y'
    
    while repeat in ['y', 'Y', 'yes', 'YES']:
        num = input("Please enter a number: ")
        print(Converter(int(num)).convert())
        repeat = input("Another number? ")
