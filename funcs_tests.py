import unittest
from fade import *
from blur import *

class TestCases(unittest.TestCase):
   # fade funcs
   def test_distance_from_pixel_to_point(self):
      self.assertEqual(distance_from_pixel_to_point((50, 70), (230, 255)), 258.11818998280614)

   # blur funcs
   def test_groups_of_3(self):
      pixels = ['5','7', '9', '13', '21', '50', '70']
      self.assertEqual(groups_of_3(pixels), [[5, 7, 9], [13, 21, 50], [70]])

if __name__ == "__main__":
   unittest.main()


