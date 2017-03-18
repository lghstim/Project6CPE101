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

   def test_get_neighbor_pixels(self):
      pixels = [[[5, 9, 100], [9, 90, 200], [59, 90, 100], [95, 25, 200]], [[25, 26, 29], [27, 29, 30], [31, 39, 41], [50, 90, 90]]]
      pixel = [5, 9, 100]
      cur_x = 0
      cur_y = 0
      neighbor_pixels = get_neighbor_pixels(pixel, cur_x, cur_y, pixels, 4)
      print(neighbor_pixels)
      self.assertEqual(neighbor_pixels, [[25, 26, 29], [9, 90, 200], [27, 29, 30], [59, 90, 100], [31, 39, 41], [95, 25, 200], [50, 90, 90]])

if __name__ == "__main__":
   unittest.main()


