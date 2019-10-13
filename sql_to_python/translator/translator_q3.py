from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 3
# SQL: SELECT empNo, mgr
# 	FROM Emp
# 	ORDER BY empNo ASC;
def query_with_order(file_path_name: Path, sheet_name: str, select_f1: str, select_f2: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}

    for row in results:
        for key in row:
            if key == select_f1 or key == select_f2:
                dict_tmp.update({key:row[key]})
        else:
            results_tmp.append(dict_tmp)
        dict_tmp = {}

    results_tmp = get_sorted_list(results_tmp,select_f1)
    results = results_tmp

    # export to output excel
    return results
