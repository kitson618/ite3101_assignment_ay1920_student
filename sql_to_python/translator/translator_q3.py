from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 3
# SQL: SELECT empNo, mgr
# 	FROM Emp
# 	ORDER BY empNo ASC;
def query_with_order(file_path_name: Path, sheet_name: str, select_f1: str, select_f2: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel
