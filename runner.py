from pathlib import Path

from sql_to_python.report.report_generator import generate_mark_report

if __name__ == '__main__':
    generate_mark_report(Path("data/test_result.zip"), Path("out/"))
