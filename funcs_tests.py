import unittest
from fade import *

class TestCases(unittest.TestCase):
   # fade funcs
   def test_distance_from_pixel_to_point(self):
      
      
      self.assertEqual(distance_from_pixel_to_point((50, 70), (230, 255)), 258.118189824)

if __name__ == "__main__":
   unittest.main()


