import unittest
from equacio1_1 import Equacio


class TestEquacio(unittest.TestCase):

    def test_positiu(self):
        eq = Equacio("2x + 3 = 7")
        self.assertEqual(eq.calcula(),2)

    def testincorrecte(self):
        eq = Equacio("2x / 3 = 7")
        self.assertEqual(eq.calcula(),"Operador no valid: "+eq.operator)
        self.assertIsInstance(eq.operator, basestring)

    def test_negatiu(self):
        eq = Equacio("2x - 3 = 7")
        self.assertEqual(eq.calcula(),5)

    def test_float(self):
        eq = Equacio("2.3x - 8.4 = 9.8")
        self.assertEqual(eq.calcula(),7.913043478260872)

    def test_caracterERROR(self):
        eq = Equacio("2x - p = 7")
        self.assertEqual(eq.calcula(),"l'equacio conte caracter no calculables o conte un string buit: "+eq.eq)

    def test_fromat_erroni(self):
        eq = Equacio("3 - 2x = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")

    def test_string_buit(self):
        eq = Equacio("3x -  = 7")
        self.assertEqual(eq.calcula(),"l'equacio conte caracter no calculables o conte un string buit: "+eq.eq)


if __name__ == '__main__':
    unittest.main()
