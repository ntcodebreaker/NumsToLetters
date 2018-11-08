from Converters import Converter

if __name__ == '__main__':
    another = 'y'
    
    while another in ['y', 'Y', 'yes', 'YES']:
        num = input("Please enter a number: ")
        print(Converter(int(num)).convert())
        another = input("Another number? ")
