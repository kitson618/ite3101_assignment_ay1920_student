import os
import unittest
from pathlib import Path


from sql_to_python.file.file_helper import read_file
from sql_to_python.result.result_generator import generate_result
from tests.test_helper import normalize_line_endings, get_worksheet


class TestTranslatorQ3(unittest.TestCase):


    def setUp(self):
        self.expected_xlsx = Path("../data/result.xlsx")


    def tearDown(self):
        excel_report_path = Path("../../out/result.xlsx")

        if excel_report_path.exists():
            os.remove(excel_report_path)


    def test_query_with_order(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q3", excel_report_path).to_dict()
        expect = get_worksheet("Q3", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
