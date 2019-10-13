import os
import shutil
from pathlib import Path

from sql_to_python.excel.tool import generate_excel
from sql_to_python.file.file_helper import unzip_to_folder, list_all_files, save_to_file, delete_folder
from sql_to_python.html.report import generate_html_report


def generate_result(source_file_path: Path, out_folder: Path) -> (str, Path):
    if out_folder.is_dir():
        shutil.rmtree(str(out_folder))

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

    # test_data
    # file = Path("../../data/source_data.xlsx")
    # query_all(file, "Emp")
    # query_with_filter(file, "Emp")
    # query_with_order(file, "Emp", "empNo", "mgr")
    # delete_record_query(file, "Emp", "eName", "MARTIN")
    # update_record_query(file, "Emp", "salary", 60000, "empNo", 7839)
    # add_table_column_query(file, "Salgrade", "diff", "hiSal", "loSal")
    # query_with_groupby(file, "Emp", "deptNo", "empNo", "job", "CLERK")
    # query_multiple_tables_A(file, "Emp", "empNo", "mgr", "empNo", "eName")
    # query_multiple_tables_B(file, "Emp", "salary", "empNo", "empNo", "eName", "salary")
    # create_table(file, "Publisher")
