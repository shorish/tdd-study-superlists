import unittest


class Something(object):
    def __init__(self):
        self.foo = 1


class TestSomething(unittest.TestCase):
    def setUp(self):
        super(TestSomething, self).setUp()
        self.something = Something()

    def test_record(self):
        self.assertTrue(1 > 0)

    def test_something_foo_equals_1(self):
        self.assertEqual(self.something.foo, 1)


if __name__ == '__main__':
    unittest.main()
