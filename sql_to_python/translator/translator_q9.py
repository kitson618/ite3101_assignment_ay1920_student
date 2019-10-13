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
                         filter_f_2: str, select_f_1: str, select_f_2: str, select_f_3: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel