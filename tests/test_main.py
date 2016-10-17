# -*- coding: utf-8 -*-
import unittest

from create_box import main


class TestCreateBox(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(1 + 1, 2)
