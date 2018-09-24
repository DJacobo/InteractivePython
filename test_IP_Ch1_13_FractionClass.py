# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_IP_Ch1_13_FractionClass.py

import unittest

from IP_Ch1_13_FractionClass import Fraction

class fractionTest(unittest.TestCase):
    def setUp(self):
        self.myF = Fraction(2, 3)
        self.yourF = Fraction(252, 105)
        self.reduceF = Fraction(2, 4) # reduces to 1/2

    def test_verify_int_error(self):
        with self.assertRaises(TypeError):
            Fraction(1.1, 2)

    def test_init_num_gcd(self):
        self.assertEqual(1, self.reduceF.getNum())

    def test_init_num_gcd_false(self):
        self.assertNotEqual(2, self.reduceF.getNum())

    def test_init_den_gdc(self):
        self.assertEqual(2, self.reduceF.getDen())

    def test_init_den_gcd_false(self):
        self.assertNotEqual(4, self.reduceF.getDen())

    def test_init_neg_bottom(self):
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))

    def test_init_neg_both(self):
        self.assertEqual(Fraction(1, 2), Fraction(-1, -2))

    def test_add_fraction(self):
        addF = Fraction(46, 15)
        self.assertTrue(addF == self.myF + self.yourF)
        
    def test_add_fraction_false(self):
        addF = Fraction(1, 2)
        self.assertNotEqual(addF, self.myF + self.yourF)
    
    def test_iadd_fraction(self):
        self.myF += self.yourF
        self.assertEqual(self.myF, Fraction(2, 3) + self.yourF)

    def test_iadd_fraction_false(self):
        self.myF += self.yourF
        self.assertNotEqual(self.myF, self.myF + self.yourF)

    def test_radd_fraction(self):
        intTest = self.myF + 4 # 2/3 + 4
        self.assertEqual(Fraction(14, 3), intTest)
        
    def test_radd_fraction_first(self):
        fracTest = 4 + self.myF
        self.assertEqual(Fraction(14, 3), fracTest)


    def test_sub_fraction(self):
        subF = Fraction(-26, 15)
        self.assertTrue(subF == self.myF - self.yourF)

    def test_sub_fraction_wrong(self):
        subF = Fraction(1, 15)
        self.assertFalse(subF == self.myF - self.yourF)

    def test_mul_fraction(self):
        mulF = Fraction(504, 315)
        self.assertTrue(mulF == self.myF * self.yourF)

    def test_mul_fraction_wrong(self):
        mulF = Fraction(1, 315)
        self.assertFalse(mulF == self.myF * self.yourF)

    def test_div_fraction(self):
        divF = Fraction(210, 756)
        self.assertTrue(divF == self.myF / self.yourF)

    def test_div_fraction_wrong(self):
        divF = Fraction(1, 756)
        self.assertFalse(divF == self.myF / self.yourF)

    def test_comp_greater(self):
        self.assertTrue(self.yourF > self.myF)

    def test_comp_greater_wrong(self):
        self.assertFalse(self.myF > self.yourF)

    def test_comp_lesser(self):
        self.assertTrue(self.myF < self.yourF)

    def test_comp_lesser_wrong(self):
        self.assertFalse(self.yourF < self.yourF)

if __name__ == '__main__':
    unittest.main()