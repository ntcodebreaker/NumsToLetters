import unittest
from Converters import Converter, getOrderOfMagnitude


class TestNumberToLetterConversions(unittest.TestCase):
    def testOnes(self):
        self.assertEqual(Converter(1).convert(), "uno")
        self.assertEqual(Converter(2).convert(), "dos")
        self.assertEqual(Converter(3).convert(), "tres")
        self.assertEqual(Converter(4).convert(), "cuatro")
        self.assertEqual(Converter(5).convert(), "cinco")
        self.assertEqual(Converter(6).convert(), "seis")
        self.assertEqual(Converter(7).convert(), "siete")
        self.assertEqual(Converter(8).convert(), "ocho")
        self.assertEqual(Converter(9).convert(), "nueve")

    def testExactTens(self):
        self.assertEqual(Converter(10).convert(), "diez")
        self.assertEqual(Converter(20).convert(), "veinte")
        self.assertEqual(Converter(30).convert(), "treinta")
        self.assertEqual(Converter(40).convert(), "cuarenta")
        self.assertEqual(Converter(50).convert(), "cincuenta")
        self.assertEqual(Converter(60).convert(), "sesenta")
        self.assertEqual(Converter(70).convert(), "setenta")
        self.assertEqual(Converter(80).convert(), "ochenta")
        self.assertEqual(Converter(90).convert(), "noventa")

    def testExceptionalCases(self):
        self.assertEqual(Converter(11).convert(), "once")
        self.assertEqual(Converter(12).convert(), "doce")
        self.assertEqual(Converter(13).convert(), "trece")
        self.assertEqual(Converter(14).convert(), "catorce")
        self.assertEqual(Converter(15).convert(), "quince")
        self.assertEqual(Converter(16).convert(), "dieciséis")
        self.assertEqual(Converter(17).convert(), "diecisiete")
        self.assertEqual(Converter(18).convert(), "dieciocho")
        self.assertEqual(Converter(19).convert(), "diecinueve")
        self.assertEqual(Converter(21).convert(), "veintiuno")
        self.assertEqual(Converter(22).convert(), "veintidós")
        self.assertEqual(Converter(23).convert(), "veintitrés")
        self.assertEqual(Converter(24).convert(), "veinticuatro")
        self.assertEqual(Converter(25).convert(), "veinticinco")
        self.assertEqual(Converter(26).convert(), "veintiséis")
        self.assertEqual(Converter(27).convert(), "veintisiete")
        self.assertEqual(Converter(28).convert(), "veintiocho")
        self.assertEqual(Converter(29).convert(), "veintinueve")

    def testTensWithRemain(self):
        self.assertEqual(Converter(31).convert(), "treinta y uno")
        self.assertEqual(Converter(42).convert(), "cuarenta y dos")
        self.assertEqual(Converter(53).convert(), "cincuenta y tres")
        self.assertEqual(Converter(64).convert(), "sesenta y cuatro")
        self.assertEqual(Converter(75).convert(), "setenta y cinco")
        self.assertEqual(Converter(86).convert(), "ochenta y seis")
        self.assertEqual(Converter(97).convert(), "noventa y siete")
        
    def testExactHundreds(self):
        self.assertEqual(Converter(100).convert(), "cien")
        self.assertEqual(Converter(200).convert(), "doscientos")
        self.assertEqual(Converter(300).convert(), "trescientos")
        self.assertEqual(Converter(400).convert(), "cuatrocientos")
        self.assertEqual(Converter(500).convert(), "quinientos")
        self.assertEqual(Converter(600).convert(), "seiscientos")
        self.assertEqual(Converter(700).convert(), "setecientos")
        self.assertEqual(Converter(800).convert(), "ochocientos")
        self.assertEqual(Converter(900).convert(), "novecientos")

    def testHundredsWithOnesRemain(self):
        self.assertEqual(Converter(101).convert(), "ciento uno")
        self.assertEqual(Converter(109).convert(), "ciento nueve")
        
    def testHundredsWithExactTensRemain(self):
        self.assertEqual(Converter(110).convert(), "ciento diez")
        self.assertEqual(Converter(190).convert(), "ciento noventa")
        self.assertEqual(Converter(910).convert(), "novecientos diez")
        self.assertEqual(Converter(990).convert(), "novecientos noventa")
        
    def testHundredsWithNonExactTensRemain(self):
        self.assertEqual(Converter(115).convert(), "ciento quince")
        self.assertEqual(Converter(229).convert(), "doscientos veintinueve")
        self.assertEqual(Converter(335).convert(), "trescientos treinta y cinco")
        self.assertEqual(Converter(999).convert(), "novecientos noventa y nueve")

    def testExactThousands(self):
        self.assertEqual(Converter(1000).convert(), "mil")
        self.assertEqual(Converter(2000).convert(), "dos mil")
        self.assertEqual(Converter(3000).convert(), "tres mil")
        self.assertEqual(Converter(4000).convert(), "cuatro mil")
        self.assertEqual(Converter(5000).convert(), "cinco mil")
        self.assertEqual(Converter(6000).convert(), "seis mil")
        self.assertEqual(Converter(7000).convert(), "siete mil")
        self.assertEqual(Converter(8000).convert(), "ocho mil")
        self.assertEqual(Converter(9000).convert(), "nueve mil")
        
    def testThousandsWithOnesRemain(self):
        self.assertEqual(Converter(1001).convert(), "mil uno")
        self.assertEqual(Converter(1005).convert(), "mil cinco")
        self.assertEqual(Converter(1009).convert(), "mil nueve")
        
    def testThousandsWithExactTensRemain(self):
        self.assertEqual(Converter(1010).convert(), "mil diez")
        self.assertEqual(Converter(5050).convert(), "cinco mil cincuenta")
        self.assertEqual(Converter(9090).convert(), "nueve mil noventa")
        
    def testThousandsWithNonExactTensRemain(self):
        self.assertEqual(Converter(1011).convert(), "mil once")
        self.assertEqual(Converter(2012).convert(), "dos mil doce")
        self.assertEqual(Converter(3029).convert(), "tres mil veintinueve")
        self.assertEqual(Converter(4045).convert(), "cuatro mil cuarenta y cinco")
        self.assertEqual(Converter(9099).convert(), "nueve mil noventa y nueve")
        
    def testThousandsWithExactHundredsRemain(self):
        self.assertEqual(Converter(1100).convert(), "mil cien")
        self.assertEqual(Converter(2200).convert(), "dos mil doscientos")
        self.assertEqual(Converter(5500).convert(), "cinco mil quinientos")
        self.assertEqual(Converter(9900).convert(), "nueve mil novecientos")
        
    def testThousandsWithNonExactHundredsRemain(self):
        self.assertEqual(Converter(1101).convert(), "mil ciento uno")
        self.assertEqual(Converter(2210).convert(), "dos mil doscientos diez")
        self.assertEqual(Converter(3311).convert(), "tres mil trescientos once")
        self.assertEqual(Converter(4429).convert(), "cuatro mil cuatrocientos veintinueve")
        self.assertEqual(Converter(9999).convert(), "nueve mil novecientos noventa y nueve")

    def testExactTensThousands(self):
        self.assertEqual(Converter(10000).convert(), "diez mil")
        self.assertEqual(Converter(20000).convert(), "veinte mil")
        self.assertEqual(Converter(30000).convert(), "treinta mil")
        self.assertEqual(Converter(40000).convert(), "cuarenta mil")
        self.assertEqual(Converter(50000).convert(), "cincuenta mil")
        self.assertEqual(Converter(60000).convert(), "sesenta mil")
        self.assertEqual(Converter(70000).convert(), "setenta mil")
        self.assertEqual(Converter(80000).convert(), "ochenta mil")
        self.assertEqual(Converter(90000).convert(), "noventa mil")

    def testTensThousandsWithOnes(self):
        self.assertEqual(Converter(10001).convert(), "diez mil uno")
        self.assertEqual(Converter(50005).convert(), "cincuenta mil cinco")
        self.assertEqual(Converter(90009).convert(), "noventa mil nueve")
        
    def testTensThousandsWithExactTens(self):
        self.assertEqual(Converter(10010).convert(), "diez mil diez")
        self.assertEqual(Converter(50050).convert(), "cincuenta mil cincuenta")
        self.assertEqual(Converter(90090).convert(), "noventa mil noventa")
        
    def testTensThousandsWithNonExactTens(self):
        self.assertEqual(Converter(10011).convert(), "diez mil once")
        self.assertEqual(Converter(50029).convert(), "cincuenta mil veintinueve")
        self.assertEqual(Converter(70065).convert(), "setenta mil sesenta y cinco")
        self.assertEqual(Converter(90099).convert(), "noventa mil noventa y nueve")

    def testTensThousandsWithExactHundreds(self):
        self.assertEqual(Converter(10100).convert(), "diez mil cien")
        self.assertEqual(Converter(50500).convert(), "cincuenta mil quinientos")
        self.assertEqual(Converter(90900).convert(), "noventa mil novecientos")
        
    def testTensThousandsWithNonExactHundreds(self):
        self.assertEqual(Converter(10101).convert(), "diez mil ciento uno")
        self.assertEqual(Converter(20210).convert(), "veinte mil doscientos diez")
        self.assertEqual(Converter(30311).convert(), "treinta mil trescientos once")
        self.assertEqual(Converter(40429).convert(), "cuarenta mil cuatrocientos veintinueve")
        self.assertEqual(Converter(50565).convert(), "cincuenta mil quinientos sesenta y cinco")
        self.assertEqual(Converter(90999).convert(), "noventa mil novecientos noventa y nueve")
        
    def testTensThousandsWithExactThousands(self):
        self.assertEqual(Converter(11000).convert(), "once mil")
        self.assertEqual(Converter(29000).convert(), "veintinueve mil")
        self.assertEqual(Converter(46000).convert(), "cuarenta y seis mil")
        self.assertEqual(Converter(99000).convert(), "noventa y nueve mil")
        
    def testTensThousandsWithNonExactThousands(self):
        self.assertEqual(Converter(11001).convert(), "once mil uno")
        self.assertEqual(Converter(22009).convert(), "veintidós mil nueve")
        self.assertEqual(Converter(33010).convert(), "treinta y tres mil diez")
        self.assertEqual(Converter(44011).convert(), "cuarenta y cuatro mil once")
        self.assertEqual(Converter(55911).convert(), "cincuenta y cinco mil novecientos once")
        self.assertEqual(Converter(99999).convert(), "noventa y nueve mil novecientos noventa y nueve")

    def testExactHundredsOfThousands(self):
        self.assertEqual(Converter(100000).convert(), "cien mil")
        self.assertEqual(Converter(200000).convert(), "doscientos mil")
        self.assertEqual(Converter(300000).convert(), "trescientos mil")
        self.assertEqual(Converter(400000).convert(), "cuatrocientos mil")
        self.assertEqual(Converter(500000).convert(), "quinientos mil")
        self.assertEqual(Converter(600000).convert(), "seiscientos mil")
        self.assertEqual(Converter(700000).convert(), "setecientos mil")
        self.assertEqual(Converter(800000).convert(), "ochocientos mil")
        self.assertEqual(Converter(900000).convert(), "novecientos mil")

    def testHundredsOfThousandsWithOnes(self):
        self.assertEqual(Converter(100001).convert(), "cien mil uno")
        self.assertEqual(Converter(900009).convert(), "novecientos mil nueve")
        
    def testHundredsOfThousandsWithExactTens(self):
        self.assertEqual(Converter(100010).convert(), "cien mil diez")
        self.assertEqual(Converter(500050).convert(), "quinientos mil cincuenta")
        self.assertEqual(Converter(900090).convert(), "novecientos mil noventa")
        
    def testHundredsOfThousandsWithNonExactTens(self):
        self.assertEqual(Converter(100011).convert(), "cien mil once")
        self.assertEqual(Converter(200029).convert(), "doscientos mil veintinueve")
        self.assertEqual(Converter(500077).convert(), "quinientos mil setenta y siete")
        self.assertEqual(Converter(900099).convert(), "novecientos mil noventa y nueve")
    
    def testHundredsOfThousandsWithExactHundreds(self):
        self.assertEqual(Converter(100100).convert(), "cien mil cien")
        self.assertEqual(Converter(200200).convert(), "doscientos mil doscientos")
        self.assertEqual(Converter(900900).convert(), "novecientos mil novecientos")
        
    def testHundredsOfThousandsWithExactThousands(self):
        self.assertEqual(Converter(101000).convert(), "ciento un mil")
        self.assertEqual(Converter(909000).convert(), "novecientos nueve mil")
        
    def testHundredsOfThousandsWithNonExactThousands(self):
        self.assertEqual(Converter(101001).convert(), "ciento un mil uno")
        self.assertEqual(Converter(202020).convert(), "doscientos dos mil veinte")
        self.assertEqual(Converter(303029).convert(), "trescientos tres mil veintinueve")
        self.assertEqual(Converter(505087).convert(), "quinientos cinco mil ochenta y siete")
        self.assertEqual(Converter(909999).convert(), "novecientos nueve mil novecientos noventa y nueve")
    
    def testNonExactHundredsOfThousands(self):
        self.assertEqual(Converter(110000).convert(), "ciento diez mil")
        self.assertEqual(Converter(220001).convert(), "doscientos veinte mil uno")
        self.assertEqual(Converter(329010).convert(), "trescientos veintinueve mil diez")
        self.assertEqual(Converter(555029).convert(), "quinientos cincuenta y cinco mil veintinueve")
        self.assertEqual(Converter(666174).convert(), "seiscientos sesenta y seis mil ciento setenta y cuatro")
        self.assertEqual(Converter(999999).convert(), "novecientos noventa y nueve mil novecientos noventa y nueve")

    def testExactMillions(self):
        self.assertEqual(Converter(1000000).convert(), "un millón")
        self.assertEqual(Converter(2000000).convert(), "dos millones")
        self.assertEqual(Converter(3000000).convert(), "tres millones")
        self.assertEqual(Converter(4000000).convert(), "cuatro millones")
        self.assertEqual(Converter(5000000).convert(), "cinco millones")
        self.assertEqual(Converter(6000000).convert(), "seis millones")
        self.assertEqual(Converter(7000000).convert(), "siete millones")
        self.assertEqual(Converter(8000000).convert(), "ocho millones")
        self.assertEqual(Converter(9000000).convert(), "nueve millones")
        
    def testMillionsWithOnes(self):
        self.assertEqual(Converter(1000001).convert(), "un millón uno")
        self.assertEqual(Converter(9000009).convert(), "nueve millones nueve")
        
    def testMillionsWithTens(self):
        self.assertEqual(Converter(1000010).convert(), "un millón diez")
        self.assertEqual(Converter(5000029).convert(), "cinco millones veintinueve")
        self.assertEqual(Converter(9000099).convert(), "nueve millones noventa y nueve")
        
    def testMillionsWithHundreds(self):
        self.assertEqual(Converter(1000100).convert(), "un millón cien")
        self.assertEqual(Converter(2000201).convert(), "dos millones doscientos uno")
        self.assertEqual(Converter(5000513).convert(), "cinco millones quinientos trece")
        self.assertEqual(Converter(9000999).convert(), "nueve millones novecientos noventa y nueve")
        
    def testMillionsWithThousands(self):
        self.assertEqual(Converter(1001000).convert(), "un millón mil")
        self.assertEqual(Converter(2002001).convert(), "dos millones dos mil uno")
        self.assertEqual(Converter(3003010).convert(), "tres millones tres mil diez")
        self.assertEqual(Converter(5005015).convert(), "cinco millones cinco mil quince")
        self.assertEqual(Converter(9009999).convert(), "nueve millones nueve mil novecientos noventa y nueve")
        
    def testMillionsWithTensOfThousands(self):
        self.assertEqual(Converter(1010000).convert(), "un millón diez mil")
        self.assertEqual(Converter(2010001).convert(), "dos millones diez mil uno")
        self.assertEqual(Converter(3010011).convert(), "tres millones diez mil once")
        self.assertEqual(Converter(4010111).convert(), "cuatro millones diez mil ciento once")
        self.assertEqual(Converter(4011111).convert(), "cuatro millones once mil ciento once")
        self.assertEqual(Converter(5029111).convert(), "cinco millones veintinueve mil ciento once")
        self.assertEqual(Converter(9099999).convert(), "nueve millones noventa y nueve mil novecientos noventa y nueve")
        
    def testMillionsWithHundredsOfThousands(self):
        self.assertEqual(Converter(1100001).convert(), "un millón cien mil uno")
        self.assertEqual(Converter(2200022).convert(), "dos millones doscientos mil veintidós")
        self.assertEqual(Converter(3300333).convert(), "tres millones trescientos mil trescientos treinta y tres")
        self.assertEqual(Converter(4404444).convert(), "cuatro millones cuatrocientos cuatro mil cuatrocientos cuarenta y cuatro")
        self.assertEqual(Converter(5555555).convert(), "cinco millones quinientos cincuenta y cinco mil quinientos cincuenta y cinco")

    def testExactTensOfMillions(self):
        self.assertEqual(Converter(10000000).convert(), "diez millones")
        self.assertEqual(Converter(20000000).convert(), "veinte millones")
        self.assertEqual(Converter(30000000).convert(), "treinta millones")
        self.assertEqual(Converter(40000000).convert(), "cuarenta millones")
        self.assertEqual(Converter(50000000).convert(), "cincuenta millones")
        self.assertEqual(Converter(60000000).convert(), "sesenta millones")
        self.assertEqual(Converter(70000000).convert(), "setenta millones")
        self.assertEqual(Converter(80000000).convert(), "ochenta millones")
        self.assertEqual(Converter(90000000).convert(), "noventa millones")
        
    def testTensOfMillionsWithOnes(self):
        self.assertEqual(Converter(10000001).convert(), "diez millones uno")
        self.assertEqual(Converter(90000009).convert(), "noventa millones nueve")
        
    def testTensOfMillionsWithTens(self):
        self.assertEqual(Converter(10000010).convert(), "diez millones diez")
        self.assertEqual(Converter(22000022).convert(), "veintidós millones veintidós")
        self.assertEqual(Converter(99000099).convert(), "noventa y nueve millones noventa y nueve")
        
    def testTensOfMillionsWithHundreds(self):
        self.assertEqual(Converter(11000100).convert(), "once millones cien")
        self.assertEqual(Converter(25000234).convert(), "veinticinco millones doscientos treinta y cuatro")
        self.assertEqual(Converter(36000909).convert(), "treinta y seis millones novecientos nueve")
        
    def testTensOfMillionsWithThousands(self):
        self.assertEqual(Converter(11001000).convert(), "once millones mil")
        self.assertEqual(Converter(22002001).convert(), "veintidós millones dos mil uno")
        self.assertEqual(Converter(33002023).convert(), "treinta y tres millones dos mil veintitrés")
        self.assertEqual(Converter(44004324).convert(), "cuarenta y cuatro millones cuatro mil trescientos veinticuatro")
        
    def testTensOfMillionsWithTensOfThousands(self):
        self.assertEqual(Converter(11012000).convert(), "once millones doce mil")
        self.assertEqual(Converter(24022001).convert(), "veinticuatro millones veintidós mil uno")
        self.assertEqual(Converter(41022001).convert(), "cuarenta y un millones veintidós mil uno")
        self.assertEqual(Converter(35022023).convert(), "treinta y cinco millones veintidós mil veintitrés")
        self.assertEqual(Converter(99099503).convert(), "noventa y nueve millones noventa y nueve mil quinientos tres")
        
    def testTensOfMillionsWithHundredsOfThousands(self):
        self.assertEqual(Converter(11212000).convert(), "once millones doscientos doce mil")
        self.assertEqual(Converter(25313001).convert(), "veinticinco millones trescientos trece mil uno")
        self.assertEqual(Converter(36431013).convert(), "treinta y seis millones cuatrocientos treinta y un mil trece")
        self.assertEqual(Converter(99999999).convert(), "noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve")

    def testExactHundredsOfMillions(self):
        self.assertEqual(Converter(100000000).convert(), "cien millones")
        self.assertEqual(Converter(200000000).convert(), "doscientos millones")
        self.assertEqual(Converter(300000000).convert(), "trescientos millones")
        self.assertEqual(Converter(400000000).convert(), "cuatrocientos millones")
        self.assertEqual(Converter(500000000).convert(), "quinientos millones")
        self.assertEqual(Converter(600000000).convert(), "seiscientos millones")
        self.assertEqual(Converter(700000000).convert(), "setecientos millones")
        self.assertEqual(Converter(800000000).convert(), "ochocientos millones")
        self.assertEqual(Converter(900000000).convert(), "novecientos millones")
        
    def testOrderOfMagnitude(self):
        self.assertEqual(getOrderOfMagnitude(0), 0)
        self.assertEqual(getOrderOfMagnitude(1), 0)
        self.assertEqual(getOrderOfMagnitude(12), 1)
        self.assertEqual(getOrderOfMagnitude(123), 2)
        self.assertEqual(getOrderOfMagnitude(1234), 3)
        self.assertEqual(getOrderOfMagnitude(12345), 4)
        self.assertEqual(getOrderOfMagnitude(123456), 5)
        self.assertEqual(getOrderOfMagnitude(1234567), 6)
        self.assertEqual(getOrderOfMagnitude(12345678), 7)
        self.assertEqual(getOrderOfMagnitude(123456789), 8)
        
    def testMaxInputNumber(self):
        with self.assertRaises(ValueError):
            Converter(1000000000).convert()
        
if __name__ == '__main__':
    unittest.main()

    #1,000,000,000
