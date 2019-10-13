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


    def test_save_to_file(self):
        expect = "testing" + os.linesep
        testfile = Path("../../out/unittest/test.txt")
        save_to_file(testfile, "testing")
        result = read_file(testfile)
        self.assertEqual(normalize_line_endings(expect), normalize_line_endings(result))


if __name__ == '__main__':
    unittest.main()
