import unittest
from employees import Employee

class TestEmployeeRaise(unittest.TestCase):
    def setUp(self):
        self.senior_employee = Employee('Antwan','Lowe',90000)
        #self.new_employee = Employee('Shanice','Matthew', '70000', 'Burkes')
        
    def test_give_default_raise(self):
        self.senior_employee.give_raise()
        self.assertEqual(self.senior_employee.salary, 95000)
        
    def test_custom_raise(self):
        self.senior_employee.give_raise(7000)
        self.assertEqual(self.senior_employee.salary, 97000)

unittest.main()
