from Converters import Converter

if __name__ == '__main__':
    keepAsking = 'y'
    
    while keepAsking in ['y', 'Y', 'yes', 'YES']:
        num = input("Please enter a number: ")
        print(Converter(int(num)).convert())
        keepAsking = input("Another number? ")
