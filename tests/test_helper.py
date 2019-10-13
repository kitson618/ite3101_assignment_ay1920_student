from pathlib import Path

import pandas as pd
from openpyxl import load_workbook


def normalize_line_endings(lines, line_ending='unix'):
    unix_newline = '\n'
    windows_newline = '\r\n'
    mac_newline = '\r'
    lines = lines.replace(windows_newline, unix_newline).replace(mac_newline, unix_newline)
    if line_ending == 'windows':
        lines = lines.replace(unix_newline, windows_newline)
    elif line_ending == 'mac':
        lines = lines.replace(unix_newline, mac_newline)
    return lines


def get_worksheet(sheet_name: str, file: Path):
    wb = load_workbook(filename=file)
    sheet_ranges = wb[sheet_name]
    df = pd.DataFrame(sheet_ranges.values)
    wb.close()
    return df
