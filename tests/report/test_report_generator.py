import os
import unittest
from pathlib import Path

from html5print import HTMLBeautifier

from sql_to_python.file.file_helper import read_file
from sql_to_python.report.report_generator import generate_mark_report
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
        html_report_content, excel_report_path = generate_mark_report(Path("../../data/test_result.zip"),
                                                                      Path("../../out/"))

        expect = HTMLBeautifier.beautify(read_file(Path("../data/result.html")))
        result = HTMLBeautifier.beautify(html_report_content)

        for i in range(0, min(len(result), len(expect))):
            self.assertEqual(expect[i], result[i])

    def test_generate_mark_report_xlsx_total_marks(self):
        html_report_content, excel_report_path = generate_mark_report(Path("../../data/test_result.zip"),
                                                                      Path("../../out/"))
        result = get_worksheet("Total Marks", excel_report_path).to_dict()
        expect = get_worksheet("Total Marks", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)

    def test_generate_mark_report_xlsx_detail_marks(self):
        html_report_content, excel_report_path = generate_mark_report(Path("../../data/test_result.zip"),
                                                                      Path("../../out/"))
        result = get_worksheet("Detail Marks", excel_report_path).to_dict()
        expect = get_worksheet("Detail Marks", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
