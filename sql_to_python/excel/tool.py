from pathlib import Path
from typing import List, Dict

import pandas as pd
import xlsxwriter
from xlsxwriter import Workbook
from sql_to_python.filter.logic import generate_data_list
from sql_to_python.translator.translator import *

# Reference:
# https://xlsxwriter.readthedocs.io/tutorial01.html
# https://xlsxwriter.readthedocs.io/worksheet.html
# https://xlsxwriter.readthedocs.io/working_with_cell_notation.html
# https://pythonspot.com/read-excel-with-pandas/
# http://www.blog.pythonlibrary.org/2018/06/06/creating-and-manipulating-pdfs-with-pdfrw/


def create_spreadsheet(sheet_name: str,workbook: Workbook):
    worksheet = workbook.get_worksheet_by_name(sheet_name)
    if worksheet is None:
        worksheet = workbook.add_worksheet(sheet_name)
    return worksheet


def generate_excel(import_path_name: Path, export_path_name: Path):
    workbook = xlsxwriter.Workbook(str(export_path_name.absolute()))

    # Q1
    result = query_all(import_path_name, "Emp")
    write_excel(result, "Q1", workbook)
    # Q2
    result = query_with_filter(import_path_name, "Emp")
    write_excel(result, "Q2", workbook)
    # Q3
    result = query_with_order(import_path_name, "Emp", "empNo", "mgr")
    write_excel(result, "Q3", workbook)
    # Q4
    result = delete_record_query(import_path_name, "Emp", "eName", "MARTIN")
    write_excel(result, "Q4", workbook)
    # Q5
    result = update_record_query(import_path_name, "Emp", "salary", 60000, "empNo", 7839)
    write_excel(result, "Q5", workbook)
    # Q6
    result = add_table_column_query(import_path_name, "Salgrade", "diff", "hiSal", "loSal")
    write_excel(result, "Q6", workbook)
    # Q7
    result = query_with_groupby(import_path_name, "Emp", "deptNo", "empNo", "job", "CLERK")
    write_excel(result, "Q7", workbook)
    # Q8
    result = query_multiple_tables_A(import_path_name, "Emp", "empNo", "mgr", "empNo", "eName")
    write_excel(result, "Q8", workbook)
    # Q9
    result = query_multiple_tables_B(import_path_name, "Emp", "salary", "empNo", "empNo", "eName", "salary")
    write_excel(result, "Q9", workbook)
    # Q10
    result = create_table(import_path_name)
    write_excel(result, "Publisher", workbook)

    workbook.close()


def write_excel(results: List[Dict[str,str]], sheet_name: str, workbook: Workbook):

    #get current sheet and update
    currentWorksheet = create_spreadsheet(sheet_name, workbook)
    header, data_list = generate_data_list(results)

    currentWorksheet.write_row('A1',header)

    for row, row_data in enumerate(data_list, start=1):
         for col, col_data in enumerate(row_data):
             currentWorksheet.write_string(row, col, col_data)


def get_excel_sheetnames(file_path_name: Path,) -> (List[str]):
    xl = pd.ExcelFile(file_path_name)
    return xl.sheet_names


def read_excel_dataframes(file_path_name: Path,sheet_name: str):
    xl = pd.ExcelFile(file_path_name)
    df = pd.read_excel(file_path_name, sheet_name=sheet_name)
    return df
