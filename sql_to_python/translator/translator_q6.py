from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 6
# SQL:
# (1) ALTER TABLE Salgrade ADD diff NUMBER DEFAULT hiSal - loSal;
# (2) SELECT * FROM Salgrade;
# => with computed value (diff = hiSal - loSal)
def add_table_column_query(file_path_name: Path, sheet_name: str, new_f: str, \
                           source_f_1: str, source_f_2: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel
