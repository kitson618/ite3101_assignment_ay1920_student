from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 2
# SQL: SELECT ename, hiredate
# 	FROM Emp
# 	WHERE hiredate LIKE '01-MAY%';
def query_with_filter(file_path_name: Path, sheet_name: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel
