import unittest

from reverse_bin import reverse_bin


class TestReverseBinary(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse_bin(13), 11)

    def test_min_value(self):
        self.assertEqual(reverse_bin(1), 1)

    def test_max_value(self):
        self.assertEqual(reverse_bin(1000000000), 1365623)
