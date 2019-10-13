import os
import unittest

from pathlib import Path
import shutil

from sql_to_python.file.file_helper import unzip_to_folder, read_file, list_all_files, save_to_file
from tests.test_helper import normalize_line_endings


class TestFileHelper(unittest.TestCase):

    def setUp(self):
        self.test_file = Path("../../out/unittest/mock_test_result/000000000/lab01/ch01_t01_hello_world.py")
        self.target_dir = Path("../../out/unittest/")
        unzip_to_folder(Path("../data/mock_test_result.zip"), Path("../../out/unittest/"))

    def tearDown(self):
        shutil.rmtree(Path("../../out/unittest/"))

    def test_unzip_to_folder(self):
        print(self.test_file.absolute())
        self.assertTrue(self.test_file.is_file())

    def test_read_file(self):
        result = read_file(self.test_file)
        expect = """============================= test session starts ==============================
platform linux -- Python 3.6.1, pytest-3.7.3, py-1.5.4, pluggy-0.7.1
rootdir: /tmp/ite3101_introduction_to_programming/tests/lab01, inifile:
collected 1 item

../../tmp/ite3101_introduction_to_programming/tests/lab01/test_ch01_t01_hello_world.py . [100%]

=========================== 1 passed in 0.08 seconds ===========================
"""
        self.assertEqual(expect, result)

    def test_list_all_files(self):
        result = list_all_files(self.target_dir)
        print(result)
        expect = [Path('../../out/unittest/mock_test_result/000000000/lab01/ch01_t01_hello_world.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t02_print_statements.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t03_strings.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t04_handling_errors.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t05_variables.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t06_arithmetic.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t07_updating_variables.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t08_comments.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t09_numbers.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t10_two_types_of_division.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t11_multi_line_strings.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t12_boolean.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab01/ch01_t13_value_error.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t01_strings.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t02_practice.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t03_escaping_characters.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t04_access_by_index.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t05_string_methods.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t06_lower.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t07_upper.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t08_str.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t09_dot_notation.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t10_printing_strings.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t11_printing_variables.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t12_string_concatenation.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t13_explicit_string_conversion.py'),
                  Path(
                      '../../out/unittest/mock_test_result/180012897/lab02/ch02_t14_string_formatting_with_percentage_1.py'),
                  Path(
                      '../../out/unittest/mock_test_result/180012897/lab02/ch02_t15_string_formatting_with_percentage_2.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab02/ch02_t16_sth_completely_familiar.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab03/ch03_t02_get_current_date_time.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab03/ch03_t03_extracting_Info.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab03/ch03_t04_hot_date.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t02_compare_closely.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t03_compare_closelier.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t04_how_tables_have_turned.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t06_and.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t07_or.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t08_not.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t09_this_n_that.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t10_mix_n_match.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t11_con_statement_syntax.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t12_if_having.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t13_else.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t14_elif.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab04/ch04_t15_big_if.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t01_ahoy.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t02_input.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t04_check_yourself_more.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t06_ay_b_c.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t07_word_up.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t08_move_it_back.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t09_ending_up.py'),
                  Path('../../out/unittest/mock_test_result/180012897/lab05/ch05_t10_test.py')]

        expect = list(map(lambda p: Path(p), expect))

        self.assertListEqual(expect, result)

    def test_save_to_file(self):
        expect = "testing" + os.linesep
        testfile = Path("../../out/unittest/test.txt")
        save_to_file(testfile, "testing")
        result = read_file(testfile)
        self.assertEqual(normalize_line_endings(expect), normalize_line_endings(result))


if __name__ == '__main__':
    unittest.main()
