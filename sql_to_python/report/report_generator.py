import os
import shutil
from pathlib import Path

from sql_to_python.excel.tool import generate_excel
from sql_to_python.file.file_helper import unzip_to_folder, list_all_files, save_to_file, delete_folder
from sql_to_python.html.report import generate_html_report
from sql_to_python.filter.logic import get_result_from_file, get_valid_and_invalid_exercise_lists


def generate_mark_report(source_file_path: Path, out_folder: Path) -> (str, Path):
    pass
