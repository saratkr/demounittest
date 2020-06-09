import unittest
## to be modified

class SimpleCalcFixturesTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        testid = self.id()
        if name == "Add":
            self.a = 10
            self.b = 20
            print (name, self.a, self.b)
            print (testid)
        if name == "sub":
            self.a = 50
            self.b = 60
            print (name, self.a, self.b)
            print(testid)

    def tearDown(self):
        print ('\n end of test', self.shortDescription())

    def test_add(self):
        """Add""" ##This is Docstrings in python
        result = self.a + self.b
        self.assertTrue(result == 30)

    def test_sub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


if __name__ == '__main__':
    unittest.main()