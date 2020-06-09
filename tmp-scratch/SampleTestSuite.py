import unittest

from .SampleSimpleCalculTests import SimpleCalcTest
from .SampleFixturesTests import SimpleCalcFixturesTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleCalcTest))
    suite.addTest(unittest.makeSuite(SimpleCalcFixturesTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
