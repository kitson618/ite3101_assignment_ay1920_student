from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 7
# SQL: SELECT deptNo, COUNT(empNo)
# 	FROM Emp
# 	WHERE job = 'CLERK'
# 	GROUP BY deptNo;
def query_with_groupby(file_path_name: Path, sheet_name: str, groupby_f: str, \
                       count_f: str, filter_f: str, filter_v: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}
    count = 0

    gropby_list = get_distinct_list(results, groupby_f)

    #read loop
    for group in gropby_list:
        for row in results:
            for key in row:
                if row[key] == group and row[filter_f] == filter_v:
                    count += 1
        if count != 0:
            dict_tmp.update({groupby_f: group})
            dict_tmp.update({"COUNT(" + count_f + ")": str(count)})
            results_tmp.append(dict_tmp)
            dict_tmp = {}
            count = 0

    results = results_tmp

    # export to output excel
    return results