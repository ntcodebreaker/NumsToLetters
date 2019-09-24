import PredefMaps

def getConverter(number):
    orderOfMagnitude = getOrderOfMagnitude(number)
    if orderOfMagnitude == 0:
        return OnesConverter(number)
    elif orderOfMagnitude == 1:
        return TensConverter(number)
    elif orderOfMagnitude == 2:
        return HundredsConverter(number)
    elif orderOfMagnitude in [3, 4, 5]:
        return ThousandsConverter(number)
    elif orderOfMagnitude > 5:
        return MillionsConverter(number)
    
        
def getOrderOfMagnitude(number):
    def getOM(number, orderOfMagnitude):
        if number == 0:
            return 0
        elif number // (10 ** orderOfMagnitude) > 0:
            return orderOfMagnitude
        else:
            return getOM(number, orderOfMagnitude - 1)
    return getOM(number, 8)
        

class Converter:
    def __init__(self, number):
        self.number = number

    def convert(self):
        try:
            if self.number > 999999999999:
                raise ValueError("Not supported number.")
            return getConverter(self.number).convert()
        except ValueError as ex:
            raise ex


class OnesConverter:
    def __init__(self, number):
        self.number = number
        
    def convert(self):
        return PredefMaps.onesMap[self.number]

        
class TensConverter:
    def __init__(self, number):
        self.remain = number % 10
        self.numOfTens = number // 10

    def convert(self):
        if self.isDivisibleByTen:
            return PredefMaps.tensMap[self.numOfTens * 10]
        elif self.isExceptionalNumber:
            return PredefMaps.exceptionsMap[(self.numOfTens * 10) + self.remain]
        else:
            tensText = self.tensText()
            return "{0} y {1}".format(tensText, self.remainText())

    @property
    def isDivisibleByTen(self):
        return self.remain == 0
        
    @property
    def isExceptionalNumber(self):
        return self.numOfTens in [1, 2] and self.remain in [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def tensText(self):
        text = Converter(self.numOfTens * 10).convert()
        return text
        
    def remainText(self):
        return Converter(self.remain).convert()
        
        
class HundredsConverter:
    def __init__(self, number):
        self.remain = number % 100
        self.numOfHdrs = number // 100

    def convert(self):
        text = self.hundredsText()
        if self.remain > 0:
            text = "{0} {1}".format(text, self.remainText())
        return text
        
    def hundredsText(self):
        text = PredefMaps.hundredsMap[self.numOfHdrs * 100]
        if self.numOfHdrs == 1 and self.remain > 0:
            text = "ciento"
        return text
        
    def remainText(self):
        return Converter(self.remain).convert()
            

class ThousandsConverter:
    def __init__(self, number):
        self.remain = number % 1000
        self.numOfThds = number // 1000
        
    def convert(self):
        text = self.thousandsText()
        if self.remain > 0:
            text = "{0} {1}".format(text, self.remainText())
        return text

    def thousandsText(self):
        text = Converter(self.numOfThds).convert()
        if text.endswith("uno"):
            text = text.replace("uno", "un") 
        if self.numOfThds == 1:
            return "mil"
        else:
            return "{0} mil".format(text)
        
    def remainText(self):
        return Converter(self.remain).convert()
            
        
class MillionsConverter:
    def __init__(self, number):
        self.remain = number % 1000000
        self.numOfMillions = number // 1000000

    def convert(self):
        text = self.millionsText()
        if self.remain > 0:
            text = "{0} {1}".format(text, self.remainText())
        return text
      
    def millionsText(self):
        text = Converter(self.numOfMillions).convert()
        if text.endswith("uno"):
            text = text.replace("uno", "un")
            
        if self.numOfMillions == 1:
            return "{0} millón".format(text)
        else:
            return "{0} millones".format(text)
            
    def remainText(self):
        return Converter(self.remain).convert()
