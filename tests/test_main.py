import unittest

from create_box import main


class TestCreateBox(unittest.TestCase):

    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), '****\n****\n****\n')

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), '@\n')

