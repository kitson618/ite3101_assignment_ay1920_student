import os
import unittest
from pathlib import Path

from html5print import HTMLBeautifier

from sql_to_python.file.file_helper import read_file
from sql_to_python.result.result_generator import generate_result
from tests.test_helper import normalize_line_endings, get_worksheet


class TestReport(unittest.TestCase):


    def setUp(self):
        self.expected_html = read_file(Path("../data/result.html"))
        self.expected_xlsx = Path("../data/result.xlsx")


    def tearDown(self):
        html_report = Path("../../out/result.html")
        excel_report_path = Path("../../out/result.xlsx")

        if html_report.exists():
            os.remove(html_report)
        if excel_report_path.exists():
            os.remove(excel_report_path)


    def test_generate_mark_report_html(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))

        expect = HTMLBeautifier.beautify(read_file(Path("../data/result.html")))
        result = HTMLBeautifier.beautify(html_report_content)

        for i in range(0, min(len(result), len(expect))):
            self.assertEqual(expect[i], result[i])


if __name__ == '__main__':
    unittest.main()
