import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr2(self):
        loc = Location("Bakersfield", 123, -456)
        self.assertEqual(repr(loc), "Location('Bakersfield', 123, -456)")

if __name__ == "__main__":
        unittest.main()
