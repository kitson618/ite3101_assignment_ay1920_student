from pathlib import Path
from typing import List, Dict

import os
import pandas as pd
import xlsxwriter
from xlsxwriter import Workbook
from xlsxwriter.utility import xl_range, xl_rowcol_to_cell

from sql_to_python.filter.logic import generate_data_list

# https://xlsxwriter.readthedocs.io/tutorial01.html
# https://xlsxwriter.readthedocs.io/worksheet.html
# https://xlsxwriter.readthedocs.io/working_with_cell_notation.html
# https://pythonspot.com/read-excel-with-pandas/
# http://www.blog.pythonlibrary.org/2018/06/06/creating-and-manipulating-pdfs-with-pdfrw/

def get_worksheet(sheet_name: str, file: Path):
    #wb = load_workbook(filename=file)
    #sheet_ranges = wb[sheet_name]
    #df = pd.DataFrame(sheet_ranges.values)
    #wb.close()
    #return df
    pass

def create_spreadsheet(sheet_name: str,workbook: Workbook):
    worksheet = workbook.get_worksheet_by_name(sheet_name)
    if worksheet is None:
        worksheet = workbook.add_worksheet(sheet_name)
    return worksheet

def generate_excel():
    pass

def close_excel(workbook: Workbook):
    pass

def write_excel(results: List[Dict[str,str]], sheet_name: str):
    file_path_name = Path("../../out/output_"+sheet_name+".xlsx")
    workbook = xlsxwriter.Workbook(str(file_path_name.absolute()))

    #get current sheet and update
    currentWorksheet = create_spreadsheet(sheet_name, workbook)
    header, data_list = generate_data_list(results)

    currentWorksheet.write_row('A1',header)

    for row, row_data in enumerate(data_list, start=1):
         for col, col_data in enumerate(row_data):
             currentWorksheet.write_string(row, col, col_data)
         #cell_range = xl_range(row, 1, row, len(row_data) - 1)
         #currentWorksheet.write(row, len(row_data), f'=SUM({cell_range})')

    #close excel
    workbook.close()

def read_excel(file_path_name: Path,sheet_name: str) -> (List[Dict[str,str]]):
    xl = pd.ExcelFile(file_path_name)
    df = pd.read_excel(file_path_name, sheet_name=sheet_name, dtype=str)
    return df.to_dict(orient='records')

def read_excel_dataframes(file_path_name: Path,sheet_name: str):
    xl = pd.ExcelFile(file_path_name)
    df = pd.read_excel(file_path_name, sheet_name=sheet_name)
    return df

def extract_data():
    pass

def generate_html(file_path_name: Path,sheet_name: str):
    xl = pd.ExcelFile(file_path_name)
    df = pd.read_excel(file_path_name, sheet_name=sheet_name)
    df.head(1)

#def generate_total_mark_worksheet(student_marks: List[List[str]], workbook: Workbook):
#    pass

#def generate_detail_marks_worksheet(headers: List[str], student_marks: List[List[str]], workbook: Workbook):
#    pass

# file = Path("../../data/source_data.xlsx")
# df_dict = read_excel(file,'Dept')
# print(df_dict)

#write_excel(["A","B","C"],df_list)

#create_spreadsheet()
#generate_html(file,'Dept')

#DataFrame : df
#Get header : df.columns.tolist()
#Get Data : df.values.tolist()