import unittest

from ..filler.models import Color

class TestColor(unittest.TestCase):

    def test_toJSON(self):
        self.assertEqual(Color("Red").toJSON(), "Red")

if __name__ == '__main__':
    unittest.main()