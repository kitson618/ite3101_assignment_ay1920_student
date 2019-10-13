from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 4
# DELETE Emp
# 	WHERE eName = 'MARTIN';
def delete_record_query(file_path_name: Path, sheet_name: str, delete_f: str, delete_v: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []

    for row in results:
        for key in row:
            if key == delete_f and row[key] == delete_v:
                break
        else:
            results_tmp.append(row)

    results = results_tmp

    # export to output excel
    return results
