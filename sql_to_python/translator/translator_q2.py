from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 2
# SQL: SELECT ename, hiredate
# 	FROM Emp
# 	WHERE hiredate LIKE '01-MAY%';
def query_with_filter(file_path_name: Path, sheet_name: str):

    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []
    for row in results:
        for key in row:
            if "05-01" in row[key]:
                results_tmp.append(row)
    results = results_tmp

    # export to output excel
    return results
