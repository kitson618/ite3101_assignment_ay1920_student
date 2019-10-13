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
                            filter_f_2: str, select_f_1: str, select_f_2: str) -> List[Dict[str,str]]:

    # get source data set

    pass

    # export to output excel