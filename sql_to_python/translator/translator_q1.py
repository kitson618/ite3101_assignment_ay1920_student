from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 1
# SQL: SELECT * FROM Emp;
def query_all(file_path_name: Path, sheet_name: str) -> List[Dict[str,str]]:

    # get source data set
    results = read_source_excel(file_path_name, sheet_name)

    # export to output excel
    return results
