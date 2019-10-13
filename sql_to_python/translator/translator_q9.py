from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 9
# SQL:
# 	SELECT e1.empNo, e1.eName, e1.salary, e2.empNo, e2.eName, e2.salary
# 	FROM Emp e1, Emp e2
# 	WHERE e1.salary = e2.salary AND e1.empNo < e2.empNo;
def query_multiple_tables_B(file_path_name: Path, sheet_name: str, filter_f_1: str, \
                         filter_f_2: str, select_f_1: str, select_f_2: str, select_f_3: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_duplicate = results
    results_tmp = []
    dict_tmp = {}

    join_list = get_distinct_list(results, filter_f_1)

    for row in results_duplicate:
        if row[filter_f_1] in join_list:
            i = row[filter_f_1]
            v_list = [d[select_f_1] for d in results if d[filter_f_1] == i and d[select_f_1] < row[select_f_1]]
            for v in v_list:
                dict_tmp.update({"P1"+select_f_1:v})
                dict_tmp.update({"P1"+select_f_2:d[select_f_2] for d in results if d[filter_f_2] == v})
                dict_tmp.update({"P1"+select_f_3:d[select_f_3] for d in results if d[filter_f_2] == v})
                dict_tmp.update({"P2"+select_f_1:row[select_f_1]})
                dict_tmp.update({"P2"+select_f_2:row[select_f_2]})
                dict_tmp.update({"P2"+select_f_3:row[select_f_3]})
                results_tmp.append(dict_tmp)
                dict_tmp = {}

    results = get_sorted_list(results_tmp,"P1"+select_f_1,"P2"+select_f_2)

    # export to output excel
    return results