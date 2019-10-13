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
    tds = "".join(map(lambda x: f"<th>{x}</th>", rows))
    return f"<tr>{tds}</tr>"


def generate_all_tr(rows: List[List[str]]) -> str:
    return "".join(map(lambda x: generate_tr(x), rows))


def generate_tr(rows: List[str]) -> str:
    tds = "".join(map(lambda x: f"<td>{x}</td>", rows))
    return f"<tr>{tds}</tr>"


def generate_html_report(file_path_name: Path) -> str:

    tbl = ""
    sheets = get_excel_sheetnames(file_path_name)

    for i in sheets:
        df = pd.read_excel(file_path_name, sheet_name=i, dtype=str)
        thead = generate_all_th(df.columns)
        trs = generate_all_tr(df.values.tolist())
        tbl += f"<div id=\"{i}\" class=\"tabcontent\"><table>{thead}{trs}</table></div>"
    template = generate_html_template(sheets)
    return HTMLBeautifier.beautify(template.replace("###table_body###", tbl))



