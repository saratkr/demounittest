import HtmlTestRunner
import unittest
import sys
sys.path.append(".") ## now you can run from up level also: >python tmp-scratch\SampleSimpleCalculTests.py
sys.path.insert(0, '..\\') ##this works. this is for running #python SampleSimpleCalculTests.py, suld be in same folder though
#  better use python -m unittest -v tmp-scratch\SampleSimpleCalculTests.py, from one-levelup folder

from calculator.simplecalculator import Calculator


class SimpleCalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('called once before any mytests in class')
        cls.cal = Calculator(0, 0)

    @classmethod
    def tearDownClass(cls):
        print('\ncalled once after all mytests in class')
        del cls.cal


    def setUp(self):
        self.cal.a = 5
        self.cal.b = 6
        print ("in setup", self.cal)

        testid = self.id().split('.')[-1]
        print ("running mytests: ", testid)
        testname = self.shortDescription()
        if testname == "Add":
            self.cal.a = 5
            self.cal.b = 6

    def tearDown(self): ##This method will only be called if the setUp() succeeds, regardless of the outcome of the test method.
        print(self.cal)



    def test_simpleadd(self):
        """Add"""
        self.assertEqual(11, self.cal.add(),"Test Failed")

    def test_addType(self):
        self.cal.a = 5.1
        self.cal.b = 5
        self.assertIs(type(1.1),type(self.cal.add()))

    def test_simplesubtract(self):
        self.assertEqual(-1,self.cal.sub())


    def test_multiply(self):
        self.assertAlmostEqual(self.cal.mul(), 30, delta=2)
        self.assertGreater(self.cal.mul(), 5)

    def test_div(self):
        self.cal.a = 5
        self.cal.b = 0
        #pass
        self.assertRaises(ZeroDivisionError, self.cal.div) ##use callable, dont call
        with self.assertRaises(TypeError):
            self.cal1 = Calculator()

html_report_dir = '..\\reports'
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
    ## the above will generate report only when run >python filename.py
    #better do it using suites
