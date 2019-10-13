import os
import unittest
from pathlib import Path

import pandas as pd
import xlsxwriter

from sql_to_python.excel.tool import generate_total_mark_worksheet, generate_detail_marks_worksheet, generate_excel
from tests.data.test_data import lab_data, headers, marks
from tests.test_helper import get_worksheet


class TestReport(unittest.TestCase):

    def setUp(self):
        self.file = Path("../../out/test.xlsx")
        self.workbook = xlsxwriter.Workbook(self.file)

    def tearDown(self):
        os.remove(self.file)

    def test_generate_detail_marks_worksheet(self):
        generate_detail_marks_worksheet(headers, marks, self.workbook)
        self.workbook.close()
        xl = pd.ExcelFile(self.file)
        df = xl.parse("Detail Marks")
        result = df.to_dict()
        expect = {'ID': {0: 123456789, 1: 987654321}, 'Lab1': {0: 12, 1: 22}, 'Lab2': {0: 13, 1: 23},
                  'Total': {0: 0, 1: 0}}
        self.assertDictEqual(expect, result)

    def test_generate_total_mark_worksheet(self):
        generate_detail_marks_worksheet(headers, marks, self.workbook)
        generate_total_mark_worksheet(marks, self.workbook)
        self.workbook.close()

        df = get_worksheet("Total Marks", self.file)

        result = df.to_dict()
        expect = {0: {0: 'id', 1: "='Detail Marks'!A2", 2: "='Detail Marks'!A3"},
                  1: {0: 'Total', 1: "='Detail Marks'!D2", 2: "='Detail Marks'!D3"}}
        self.assertDictEqual(expect, result)

    def test_generate_excel(self):
        generate_excel(self.file, lab_data)
        xl = pd.ExcelFile(self.file)
        df = xl.parse("Detail Marks")
        result = df.to_dict()
        expect = {'id/lab': {0: 180031132, 1: 180074586}, 'Lab01': {0: 0, 1: 12}, 'Lab02': {0: 0, 1: 16},
                  'Lab03': {0: 0, 1: 6}, 'Lab04': {0: 4, 1: 13}, 'Lab05': {0: 5, 1: 9}, 'Total': {0: 0, 1: 0}}
        self.assertDictEqual(expect, result)

        df = get_worksheet("Total Marks", self.file)

        result = df.to_dict()
        expect = {0: {0: 'id', 1: "='Detail Marks'!A2", 2: "='Detail Marks'!A3"},
                  1: {0: 'Total', 1: "='Detail Marks'!G2", 2: "='Detail Marks'!G3"}}
        self.assertDictEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
