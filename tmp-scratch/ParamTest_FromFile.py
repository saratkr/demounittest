import unittest, sys, json
sys.path.append(".")
sys.path.insert(0, '..\\')
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class, param

## use ddt - pip install ddt (to be done)
@parameterized.expand(
    param.explicit(json.loads(line))
    for line in open("file1.txt")
)
class MyTestCase(unittest.TestCase):


    def test_something(self, value, onclick):
        print (value)


if __name__ == '__main__':
    unittest.main()
