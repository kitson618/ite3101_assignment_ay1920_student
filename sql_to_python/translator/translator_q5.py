from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 5
# SQL:
# (1) UPDATE Emp
# 	SET salary = 60000
# 	WHERE empNo =7839;
def update_record_query(file_path_name: Path, sheet_name: str, update_f: str, \
                        update_v: int, filter_f: str, filter_v: int):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []

    for row in results:
        for key in row:
            if key == filter_f and row[key] == str(filter_v):
                row[update_f] = str(update_v)
        results_tmp.append(row)

    results = results_tmp

    # export to output excel
    return results
