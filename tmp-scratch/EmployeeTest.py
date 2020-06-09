import unittest
from unittest.mock import MagicMock, patch, Mock
import sys
sys.path.insert(0, '..\\')
from employee.Employee import Employee, EmpDetails


class TestEmployee(unittest.TestCase):

    #When a function is decorated using @patch, a mock of the class, method or function passed as the target to @patch is returned and passed as an argument
    # to the decorated function.
    @patch('employee.Employee.Employee')
    def test_empcount_with_mock(self, MockEmp):
        emp = MockEmp()
        emp.getCount.return_value = 155
        self.emp_detail = EmpDetails(emp)
        #print (emp.getCount())
        #print(self.emp_detail.checkTotalEmployee())
        self.assertEqual(self.emp_detail.checkTotalEmployee(), "All good")


    def test_with_magicmock(self):
        emp = Employee()
        emp.getCount = MagicMock(return_value=1500)
        print(emp.getCount())
        self.empdetail = EmpDetails(emp)
        self.assertEqual(self.empdetail.checkTotalEmployee(), "Too congested")

if __name__ == '__main__':
    unittest.main()

#https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
#https://stackoverflow.com/questions/16060724/patch-why-wont-the-relative-patch-target-name-work
#https://docs.python.org/3/library/unittest.mock.html