import unittest
import sys
import import_ipynb
from Finding_the_Length_of_the_Polar_Spiral_Curve import *

class Test(unittest.TestCase):
    
    def test_r(self):
        self.assertAlmostEqual(r(24*pi),16.0,1)

    def test_opposite(self):
        self.assertAlmostEqual(opposite(r(0),r(0.0001),0.0001),0.0003,4)

    def test_trap_integral(self):
        self.assertAlmostEqual(spiral(r,0,2*pi*12),716.4,1)


if __name__ == '__main__':
    unittest.main()
