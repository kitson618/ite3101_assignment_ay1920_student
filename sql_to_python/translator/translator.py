from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list


def read_source_excel(file_path_name: Path, sheet_name: str) -> (List[Dict[str, str]]):
    xl = pd.ExcelFile(file_path_name)
    df = pd.read_excel(file_path_name, sheet_name=sheet_name, dtype=str)
    return df.to_dict(orient='records')

