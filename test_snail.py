import unittest

from snail import Snail


class TestSnail(unittest.TestCase):

    def test_3x3(self):
        snail = Snail(3, 3)
        self.assertEqual(snail.get_way(), [(2, 1), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)])

    def test_4x1(self):
        snail = Snail(4, 2)
        self.assertEqual(snail.get_way(), [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 0), (2, 0), (1, 0)])
