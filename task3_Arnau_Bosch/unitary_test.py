import unittest
from equacio1_1 import Equacio

class TestEq1_1(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(Equacio('20x + 30 = 70').calcula(), 2.0)
        varA = Equacio.a
        self.assertEqual(varA, "20")

if __name__ == "__main__":

    unittest.main()
