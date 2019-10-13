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
                        update_v: int, filter_f: str, filter_v: int) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel
