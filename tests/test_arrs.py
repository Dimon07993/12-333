import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3]
        self.assertEqual(arrs.get(array, 1), 2)

    def test_get_non_existing_index(self):
        array = [1, 2, 3]
        self.assertEqual(arrs.get(array, 5), None)

    def test_get_default_value(self):
        array = [1, 2, 3]
        self.assertEqual(arrs.get(array, 5, "default"), "default")

    def test_get_empty_array(self):
        array = []
        self.assertEqual(arrs.get(array, 0), None)

    def test_slice_whole_array(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array), [1, 2, 3, 4, 5])

    def test_slice_start_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, 2), [3, 4, 5])

    def test_slice_end_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, end=3), [1, 2, 3])

    def test_slice_start_and_end_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, 1, 4), [2, 3, 4])

    def test_slice_negative_start_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, -3), [3, 4, 5])

    def test_slice_negative_end_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrs.my_slice(array, end=-2), [1, 2, 3])

