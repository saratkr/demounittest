import unittest
import sys
sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class


@parameterized_class(("a", "b", "expected_sum", "expected_sub"), [
   (7, -1, 6, 8),
   (4, -2.2, 1.8, 6.2 )
])
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("In setupclass() method")
        cls.cal = Calculator(4, 3)

    def setUp(self):
        self.cal.a = self.a
        self.cal.b = self.b


    def test_add(self):
        self.assertAlmostEqual(self.cal.add(), self.expected_sum, delta=2)


    # @parameterized.expand([
    #     (-1.5, -2.0, -3.5),
    #     (2, 1.0, 3),
    #     (1.6, 1, 2.6),
    #     (-8,5,-3)
    # ])
    # def test_add_something(self, in1, in2, out):
    #     self.cal.a = in1
    #     self.cal.b = in2
    #     self.assertEqual(self.cal.add(), out)


if __name__ == '__main__':
    unittest.main()
