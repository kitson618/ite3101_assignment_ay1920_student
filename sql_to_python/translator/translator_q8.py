from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 8
# SQL: SELECT Sup.empNo AS "Supervisor", Sup.eName AS "SupName",
# 		Sub.empNo AS "Subordinate", Sub.eName AS "SubName"
# 	    FROM Emp Sup, Emp Sub
# 	    WHERE Sup.empNo = Sub.mgr
def query_multiple_tables_A(file_path_name: Path, sheet_name: str, filter_f_1: str, \
                            filter_f_2: str, select_f_1: str, select_f_2: str):

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)
    results_duplicate = results
    results_tmp = []
    dict_tmp = {}

    join_list = get_distinct_list(results, filter_f_1)

    for row in results_duplicate:
        for key in row:
            if key == filter_f_2 and row[filter_f_2] in join_list:
                i = row[filter_f_2]
                v1 = [d[select_f_1] for d in results if d[select_f_1] == i].pop()
                v2 = [d[select_f_2] for d in results if d[select_f_1] == i].pop()
                dict_tmp.update({"Parent":v1})
                dict_tmp.update({"PName":v2})
                dict_tmp.update({"Child":row[select_f_1]})
                dict_tmp.update({"CName":row[select_f_2]})
                results_tmp.append(dict_tmp)
                dict_tmp = {}

    results = get_sorted_list(results_tmp,"Parent","Child")

    # export to output excel
    return results