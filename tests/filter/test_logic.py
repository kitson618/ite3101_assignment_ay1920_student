import os
import unittest
from pathlib import Path

from sql_to_python.filter.logic import get_distinct_list, generate_data_list, get_sorted_list_singular, get_sorted_list
from tests.data.test_data import test_data


class TestLogic(unittest.TestCase):


    def test_get_distinct_list(self):
        data = [{'id': '123456789', 'lab': 'Lab03', 'exercise': 'Task 10 Two Types Of Division', 'status': 'Failed'},
                {'id': '123456789', 'lab': 'Lab01', 'exercise': ' Init  ', 'status': 'Invalid'},
                {'id': '000000000', 'lab': 'Lab01', 'exercise': 'Task 01 Hello World', 'status': 'OK'}]
        expect = ['000000000', '123456789']
        result = get_distinct_list(data, "id")
        self.assertListEqual(expect, result)
        expect = ['Lab01', 'Lab03']
        result = get_distinct_list(data, "lab")
        self.assertListEqual(expect, result)
        expect = [' Init  ', 'Task 01 Hello World', 'Task 10 Two Types Of Division']
        result = get_distinct_list(data, "exercise")
        self.assertListEqual(expect, result)


    def test_get_sorted_list_singular(self):
        expect = [{'empNo': '7876', 'eName': 'ADAMS', 'job': 'CLERK', 'mgr': '7788', 'hireDate': '1987-05-23 00:00:00', 'salary': '1100', 'comm': '', 'deptNo': '20', 'dummy': '10'},
                  {'empNo': '7782', 'eName': 'CLARK', 'job': 'MANAGER', 'mgr': '7839', 'hireDate': '1981-06-09 00:00:00', 'salary': '2450', 'comm': '', 'deptNo': '10', 'dummy': '6'},
                  {'empNo': '7902', 'eName': 'FORD', 'job': 'ANALYST', 'mgr': '7566', 'hireDate': '1981-12-03 00:00:00', 'salary': '3000', 'comm': '', 'deptNo': '20', 'dummy': '12'},
                  {'empNo': '7566', 'eName': 'JONES', 'job': 'MANAGER', 'mgr': '7839', 'hireDate': '1981-04-02 00:00:00', 'salary': '2975', 'comm': '', 'deptNo': '20', 'dummy': '1'},
                  {'empNo': '7839', 'eName': 'KING', 'job': 'PRESIDENT', 'mgr': '', 'hireDate': '1981-11-17 00:00:00', 'salary': '5000', 'comm': '', 'deptNo': '10', 'dummy': '8'},
                  {'empNo': '7934', 'eName': 'MILLER', 'job': 'CLERK', 'mgr': '7782', 'hireDate': '1982-01-23 00:00:00', 'salary': '1300', 'comm': '', 'deptNo': '10', 'dummy': '13'},
                  {'empNo': '7788', 'eName': 'SCOTT', 'job': 'ANALYST', 'mgr': '7566', 'hireDate': '1987-04-19 00:00:00', 'salary': '3000', 'comm': '', 'deptNo': '20', 'dummy': '14'},
                  {'empNo': '7369', 'eName': 'SMITH', 'job': 'CLERK', 'mgr': '7902', 'hireDate': '1980-12-17 00:00:00', 'salary': '800', 'comm': '', 'deptNo': '20', 'dummy': '7'}]
        result = get_sorted_list_singular(test_data, 'eName')
        self.assertListEqual(expect, result)


    def test_get_sorted_list(self):
        expect = [{'empNo': '7934', 'eName': 'MILLER', 'job': 'CLERK', 'mgr': '7782', 'hireDate': '1982-01-23 00:00:00', 'salary': '1300', 'comm': '', 'deptNo': '10', 'dummy': '13'},
                  {'empNo': '7782', 'eName': 'CLARK', 'job': 'MANAGER', 'mgr': '7839', 'hireDate': '1981-06-09 00:00:00', 'salary': '2450', 'comm': '', 'deptNo': '10', 'dummy': '6'},
                  {'empNo': '7839', 'eName': 'KING', 'job': 'PRESIDENT', 'mgr': '', 'hireDate': '1981-11-17 00:00:00', 'salary': '5000', 'comm': '', 'deptNo': '10', 'dummy': '8'},
                  {'empNo': '7876', 'eName': 'ADAMS', 'job': 'CLERK', 'mgr': '7788', 'hireDate': '1987-05-23 00:00:00', 'salary': '1100', 'comm': '', 'deptNo': '20', 'dummy': '10'},
                  {'empNo': '7566', 'eName': 'JONES', 'job': 'MANAGER', 'mgr': '7839', 'hireDate': '1981-04-02 00:00:00', 'salary': '2975', 'comm': '', 'deptNo': '20', 'dummy': '1'},
                  {'empNo': '7902', 'eName': 'FORD', 'job': 'ANALYST', 'mgr': '7566', 'hireDate': '1981-12-03 00:00:00', 'salary': '3000', 'comm': '', 'deptNo': '20', 'dummy': '12'},
                  {'empNo': '7788', 'eName': 'SCOTT', 'job': 'ANALYST', 'mgr': '7566', 'hireDate': '1987-04-19 00:00:00', 'salary': '3000', 'comm': '', 'deptNo': '20', 'dummy': '14'},
                  {'empNo': '7369', 'eName': 'SMITH', 'job': 'CLERK', 'mgr': '7902', 'hireDate': '1980-12-17 00:00:00', 'salary': '800', 'comm': '', 'deptNo': '20', 'dummy': '7'}]
        result = get_sorted_list(test_data, 'deptNo', 'salary')
        self.assertListEqual(expect, result)


    def test_generate_data_list(self):
        expect_header = ['empNo', 'eName', 'job', 'mgr', 'hireDate', 'salary', 'comm', 'deptNo', 'dummy']
        expect_datalist = [['7566', 'JONES', 'MANAGER', '7839', '1981-04-02 00:00:00', '2975', '', '20', '1'],
                            ['7782', 'CLARK', 'MANAGER', '7839', '1981-06-09 00:00:00', '2450', '', '10', '6'],
                            ['7369', 'SMITH', 'CLERK', '7902', '1980-12-17 00:00:00', '800', '', '20', '7'],
                            ['7839', 'KING', 'PRESIDENT', '', '1981-11-17 00:00:00', '5000', '', '10', '8'],
                            ['7876', 'ADAMS', 'CLERK', '7788', '1987-05-23 00:00:00', '1100', '', '20', '10'],
                            ['7902', 'FORD', 'ANALYST', '7566', '1981-12-03 00:00:00', '3000', '', '20', '12'],
                            ['7934', 'MILLER', 'CLERK', '7782', '1982-01-23 00:00:00', '1300', '', '10', '13'],
                            ['7788', 'SCOTT', 'ANALYST', '7566', '1987-04-19 00:00:00', '3000', '', '20', '14']]

        result_header, result_datalist = generate_data_list(test_data)

        self.assertListEqual(expect_header, result_header)
        self.assertListEqual(expect_datalist, result_datalist)


if __name__ == '__main__':
    unittest.main()
