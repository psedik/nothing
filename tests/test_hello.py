import unittest

from nothing.manage import hello


class Tests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello("Jan"), "Hello Jan!")
        self.assertEqual(hello(None), None)
