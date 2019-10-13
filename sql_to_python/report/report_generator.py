import os
import shutil
from pathlib import Path

from sql_to_python.excel.tool import generate_excel
from sql_to_python.file.file_helper import unzip_to_folder, list_all_files, save_to_file, delete_folder
from sql_to_python.html.report import generate_html_report
from sql_to_python.filter.logic import get_result_from_file, get_valid_and_invalid_exercise_lists


def generate_mark_report(source_file_path: Path, out_folder: Path) -> (str, Path):
    if out_folder.is_dir():
        shutil.rmtree(str(out_folder))

    unzip_to_folder(source_file_path, out_folder)
    files = list_all_files(out_folder)

    results = list(map(get_result_from_file, files))
    valid, invalid = get_valid_and_invalid_exercise_lists(results)

    html_report = out_folder.joinpath("result.html")
    excel_report_path = out_folder.joinpath("result.xlsx")

    if html_report.exists():
        os.remove(str(html_report))
    if excel_report_path.exists():
        os.remove(str(excel_report_path))

    html_report_content = generate_html_report(valid)
    save_to_file(html_report, html_report_content)
    generate_excel(excel_report_path, valid)
    delete_folder(out_folder.joinpath("test_result"))
    return html_report_content, excel_report_path

