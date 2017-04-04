import unittest


def fun():
    return 1


class test_init(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(), 1)
