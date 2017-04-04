import unittest


def fun():
    return 1


class InitTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(), 1)
