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


    def test_query_all(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q1", excel_report_path).to_dict()
        expect = get_worksheet("Q1", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_query_with_filter(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q2", excel_report_path).to_dict()
        expect = get_worksheet("Q2", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_query_with_order(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q3", excel_report_path).to_dict()
        expect = get_worksheet("Q3", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_delete_record_query(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q4", excel_report_path).to_dict()
        expect = get_worksheet("Q4", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_update_record_query(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q5", excel_report_path).to_dict()
        expect = get_worksheet("Q5", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_update_record_query(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q5", excel_report_path).to_dict()
        expect = get_worksheet("Q5", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_add_table_column_query(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q6", excel_report_path).to_dict()
        expect = get_worksheet("Q6", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_query_with_groupby(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q7", excel_report_path).to_dict()
        expect = get_worksheet("Q7", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_query_multiple_tables_A(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q8", excel_report_path).to_dict()
        expect = get_worksheet("Q8", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_query_multiple_tables_B(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Q9", excel_report_path).to_dict()
        expect = get_worksheet("Q9", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


    def test_create_table(self):
        html_report_content, excel_report_path = generate_result(Path("../../data/source_data.zip"),
                                                                 Path("../../out/"))
        result = get_worksheet("Publisher", excel_report_path).to_dict()
        expect = get_worksheet("Publisher", self.expected_xlsx).to_dict()

        self.assertDictEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
