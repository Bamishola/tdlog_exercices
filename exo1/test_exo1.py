import unittest

from exo1 import premier


class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        premier1 = premier(4)

        self.assertFalse(premier1)


if __name__ == '__main__':
    unittest.main()
