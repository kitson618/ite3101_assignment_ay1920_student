import os
import shutil
from pathlib import Path

from sql_to_python.excel.tool import generate_excel
from sql_to_python.file.file_helper import unzip_to_folder, list_all_files, save_to_file, cleanup_folder
from sql_to_python.html.report import generate_html_report


def generate_result(source_file_path: Path, out_folder: Path) -> (str, Path):
    if out_folder.is_dir():
        cleanup_folder(str(out_folder))

    unzip_to_folder(source_file_path, out_folder)
    files = list_all_files(out_folder)

    source_data_path = out_folder.joinpath(files[0])
    excel_report_path = out_folder.joinpath("result.xlsx")
    html_report = out_folder.joinpath("result.html")

    if html_report.exists():
        os.remove(str(html_report))
    if excel_report_path.exists():
        os.remove(str(excel_report_path))

    generate_excel(source_data_path, excel_report_path)

    html_report_content = generate_html_report(excel_report_path)
    save_to_file(html_report, html_report_content)

    return html_report_content, excel_report_path
