import os
import unittest
from pathlib import Path

from sql_to_python.filter.logic import is_test_passed, split_path, get_friendly_exercise_name, get_result_from_file, \
    get_valid_and_invalid_exercise_lists, get_distinct_list, generate_lab_mark
from tests.data.test_data import lab_data


class TestLogic(unittest.TestCase):
    def test_is_test_passed_true(self):
        self.assertTrue(is_test_passed(Path("../data/passed_test_result.txt")))

    def test_is_test_passed_false(self):
        self.assertFalse(is_test_passed(Path("../data/failed_test_result.txt")))

    def test_split_path(self):
        result = split_path(Path(f"a{os.path.sep}b{os.path.sep}c"))
        expect = ["a", "b", "c"]
        self.assertListEqual(expect, result)

    def test_get_friendly_exercise_name(self):
        result = get_friendly_exercise_name("ch01_t01_hello_world")
        expect = "Task 01 Hello World"
        self.assertEqual(expect, result)

    def test_get_result_from_file_ok(self):
        result = get_result_from_file(Path("../data/test_result/000000000/lab01/ch01_t01_hello_world"))
        expect = {'id': '000000000', 'lab': 'Lab01', 'exercise': 'Task 01 Hello World', 'status': 'OK'}
        self.assertDictEqual(expect, result)

    def test_get_result_from_file_failed(self):
        result = get_result_from_file(Path("../data/test_result/123456789/lab01/ch01_t10_two_types_of_division"))
        expect = {'id': '123456789', 'lab': 'Lab01', 'exercise': 'Task 10 Two Types Of Division', 'status': 'Failed'}
        self.assertDictEqual(expect, result)

    def test_get_result_from_file_invalid(self):
        result = get_result_from_file(Path("../data/test_result/123456789/lab01/__init__"))
        expect = {'id': '123456789', 'lab': 'Lab01', 'exercise': ' Init  ', 'status': 'Invalid'}
        self.assertDictEqual(expect, result)

    def test_get_valid_and_invalid_exercise_lists(self):
        data = [{'id': '000000000', 'lab': 'Lab01', 'exercise': 'Task 01 Hello World', 'status': 'OK'},
                {'id': '123456789', 'lab': 'Lab01', 'exercise': 'Task 10 Two Types Of Division', 'status': 'Failed'},
                {'id': '123456789', 'lab': 'Lab01', 'exercise': ' Init  ', 'status': 'Invalid'}]

        valid, invalid = get_valid_and_invalid_exercise_lists(data)
        expected_valid = [{'id': '000000000', 'lab': 'Lab01', 'exercise': 'Task 01 Hello World', 'status': 'OK'},
                          {'id': '123456789', 'lab': 'Lab01', 'exercise': 'Task 10 Two Types Of Division',
                           'status': 'Failed'}]
        self.assertListEqual(expected_valid, valid)
        expected_invalid = [{'id': '123456789', 'lab': 'Lab01', 'exercise': ' Init  ', 'status': 'Invalid'}]
        self.assertListEqual(expected_invalid, invalid)

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

    def test_generate_lab_mark(self):
        result = generate_lab_mark(lab_data)
        expect = (['id/lab', 'Lab01', 'Lab02', 'Lab03', 'Lab04', 'Lab05'],
                  [['180031132', '0', '0', '0', '4', '5'], ['180074586', '12', '16', '6', '13', '9']])
        self.assertTupleEqual(expect, result)










# def get_distinct_list(results: List[Dict[str, str]], key: str) -> List[str]:
#     distinct = list(set(map(lambda x: x[key], results)))
#     List.sort(distinct)
#     return distinct
#
#
# def get_sorted_list_singular(results: List[Dict[str,str]], key: str) -> List[Dict[str,str]]:
#     results = sorted(results, key=lambda x: (x[key]))
#     return results
#
#
# def get_sorted_list(results: List[Dict[str,str]], *args: str) -> List[Dict[str,str]]:
#     # allow multiple sort keys
#     results = sorted(results, key=lambda x: ([x[key] for key in args]))
#     return results
#
#
# def generate_data_list(results: List[Dict[str, str]]) -> (List[str], List[List[str]]):
#     datalist, tmplist, header = [], [], []
#
#     for row in results:
#         for key in row:
#             if results.index(row) == 0:
#                 header.append(key)
#             tmplist.append(row[key])
#         datalist.append(tmplist)
#         tmplist = []
#
#     return header, datalist


if __name__ == '__main__':
    unittest.main()
