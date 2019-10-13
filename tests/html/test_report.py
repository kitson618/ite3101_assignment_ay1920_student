import unittest
from pathlib import Path

from sql_to_python.file.file_helper import read_file
from sql_to_python.html.report import generate_tr, generate_all_tr, generate_all_th, generate_html_template, generate_html_report
from tests.data.test_data import test_data, headers, html_headers, results
from tests.test_helper import normalize_line_endings


class TestReport(unittest.TestCase):

    def setUp(self):
        self.source_xlsx = Path("../data/test_data.xlsx")


    def test_generate_tr(self):
        result = generate_tr(headers)
        expect = "<tr><td>empNo</td><td>eName</td><td>job</td><td>mgr</td><td>hireDate</td><td>salary</td><td>comm</td><td>deptNo</td><td>dummy</td></tr>"
        self.assertEqual(expect, result)


    def test_generate_all_th(self):
        result = generate_all_th(headers)
        expect = "<tr><th>empNo</th><th>eName</th><th>job</th><th>mgr</th><th>hireDate</th><th>salary</th><th>comm</th><th>deptNo</th><th>dummy</th></tr>"


    def test_generate_all_tr(self):
        result = generate_all_tr(results)
        expect = "<tr><td>NE</td><td>1</td><td>Hong Kong</td></tr><tr><td>OR</td><td>2</td><td>Taiwan</td></tr>"
        self.assertEqual(expect, result)


    def test_generate_html_template(self):
        result = generate_html_template(html_headers)
        expect = """<!DOCTYPE html>
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
<button class="tablinks" onclick="openQuestion(event, 'Q1')">Q1</button><button class="tablinks" onclick="openQuestion(event, 'Q2')">Q2</button>
</div>
<!-- table content -->
###table_body###
</body>
</html>"""
        self.assertEqual(expect, result)


    def test_generate_html_report(self):
        result = generate_html_report(self.source_xlsx)
        expect = """<!DOCTYPE html>
<html>
  <head>
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <link href="../sql_to_python/html/style.css" rel="stylesheet" type="text/css">
    <script src="../sql_to_python/html/tab.js" type="text/javascript">
    </script>
  </head>
  <body>
    <h2>
      SQL - Python Translator
    </h2>
    <!-- tab -->
    <div class="tab">
      <button class="tablinks" onclick="openQuestion(event, 'Dept')">
    Dept
      </button>
      <button class="tablinks" onclick="openQuestion(event, 'Emp')">
        Emp
      </button>
    </div>
    <!-- table content -->
    <div class="tabcontent" id="Dept">
      <table>
        <tbody>
          <tr>
            <th>
       deptNo
            </th>
            <th>
              dName
            </th>
          </tr>
          <tr>
            <td>
              10
            </td>
            <td>
              ACCOUNTING
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="tabcontent" id="Emp">
      <table>
        <tbody>
          <tr>
            <th>
              empNo
            </th>
            <th>
              eName
            </th>
          </tr>
          <tr>
            <td>
              7566
            </td>
            <td>
              JONES
            </td>
          </tr>
          <tr>
            <td>
              7782
            </td>
            <td>
              CLARK
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>
"""
        self.assertEqual(normalize_line_endings(expect), normalize_line_endings(result))


if __name__ == '__main__':
    unittest.main()
