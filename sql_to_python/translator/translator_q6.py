from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 6
# SQL:
# (1) ALTER TABLE Salgrade ADD diff NUMBER DEFAULT hiSal - loSal;
# (2) SELECT * FROM Salgrade;
# => with computed value (diff = hiSal - loSal)
def add_table_column_query(file_path_name: Path, sheet_name: str, new_f: str, \
                           source_f_1: str, source_f_2: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}
    v1 = v2 = 0

    for row in results:
        for key in row:
            dict_tmp.update({key:row[key]})
            if(key==source_f_1):
                v1 = int(row[source_f_1])
            elif(key==source_f_2):
                v2 = int(row[source_f_2])
        else:
            dict_tmp.update({new_f:str(abs(v1-v2))})
        results_tmp.append(dict_tmp)
        dict_tmp = {}

    results = results_tmp

    # export to output excel
    return results
