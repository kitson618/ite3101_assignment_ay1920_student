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
                       count_f: str, filter_f: str, filter_v: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel