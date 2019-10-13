from typing import List, Dict

import pandas as pd
from pathlib import Path
from sql_to_python.excel.tool import get_excel_sheetnames
from html5print import HTMLBeautifier
# Reference:
# https://pypi.org/project/html5print/


def generate_html_template(headers: List[str]) -> str:
    tab = "".join(map(lambda x: f"<button class=\"tablinks\" onclick=\"openQuestion(event, '{x}')\">{x}</button>", headers))
    return f"""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="../sql_to_python/html/style.css">
<script type="text/javascript" src="../sql_to_python/html/tab.js"></script>
</head>
<body>
<h2>SQL - Python Translator</h2>
<!-- tab -->
<div class="tab">
{tab}
</div>
<!-- table content -->
###table_body###
</body>
</html>"""


def generate_all_th(rows: List[str]) -> str:
    pass


def generate_all_tr(rows: List[List[str]]) -> str:
    pass


def generate_tr(rows: List[str]) -> str:
    pass


def generate_html_report(file_path_name: Path) -> str:
    pass



