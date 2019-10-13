import os
import unittest
from pathlib import Path

import pandas as pd
import xlsxwriter

from sql_to_python.excel.tool import generate_excel, write_excel
from tests.data.test_data import test_data, headers
from tests.test_helper import get_worksheet


class TestReport(unittest.TestCase):

    def setUp(self):
        self.file = Path("../../out/test.xlsx")
        self.workbook = xlsxwriter.Workbook(self.file)

    def tearDown(self):
        os.remove(self.file)


    def test_write_excel(self):
        workbook = xlsxwriter.Workbook(str(self.file.absolute()))
        write_excel(test_data,"Emp",workbook)
        workbook.close()
        xl = pd.ExcelFile(self.file)
        df = pd.read_excel(self.file, sheet_name="Emp", dtype=str)
        result = df.replace('nan', '').to_dict()
        print(result)
        expect = {'empNo': {0: '7566', 1: '7782', 2: '7369', 3: '7839', 4: '7876', 5: '7902', 6: '7934', 7: '7788'}, 'eName': {0: 'JONES', 1: 'CLARK', 2: 'SMITH', 3: 'KING', 4: 'ADAMS', 5: 'FORD', 6: 'MILLER', 7: 'SCOTT'}, 'job': {0: 'MANAGER', 1: 'MANAGER', 2: 'CLERK', 3: 'PRESIDENT', 4: 'CLERK', 5: 'ANALYST', 6: 'CLERK', 7: 'ANALYST'}, 'mgr': {0: '7839', 1: '7839', 2: '7902', 3: '', 4: '7788', 5: '7566', 6: '7782', 7: '7566'}, 'hireDate': {0: '1981-04-02 00:00:00', 1: '1981-06-09 00:00:00', 2: '1980-12-17 00:00:00', 3: '1981-11-17 00:00:00', 4: '1987-05-23 00:00:00', 5: '1981-12-03 00:00:00', 6: '1982-01-23 00:00:00', 7: '1987-04-19 00:00:00'}, 'salary': {0: '2975', 1: '2450', 2: '800', 3: '5000', 4: '1100', 5: '3000', 6: '1300', 7: '3000'}, 'comm': {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: ''}, 'deptNo': {0: '20', 1: '10', 2: '20', 3: '10', 4: '20', 5: '20', 6: '10', 7: '20'}, 'dummy': {0: '1', 1: '6', 2: '7', 3: '8', 4: '10', 5: '12', 6: '13', 7: '14'}}
        self.assertDictEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
