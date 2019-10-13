import unittest

from sql_to_python.html.report import generate_tr, generate_all_tr, generate_html_template, generate_html_report
from tests.data.test_data import lab_data, headers, marks
from tests.test_helper import normalize_line_endings


class TestReport(unittest.TestCase):

    def test_generate_tr(self):
        result = generate_tr(headers)
        expect = "<tr><td>ID</td><td>Lab1</td><td>Lab2</td></tr>"
        self.assertEqual(expect, result)

    def test_generate_all_tr(self):
        result = generate_all_tr(marks)
        expect = "<tr><td>123456789</td><td>12</td><td>13</td></tr><tr><td>987654321</td><td>22</td><td>23</td></tr>"
        self.assertEqual(expect, result)

    def test_generate_html_template(self):
        result = generate_html_template(headers)
        expect = """<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<title>Lab Marks</title>
<style>
table {
    border-collapse: collapse;
    width: 100%;
}
th, td {
    text-align: left;
    padding: 8px;
}
tr:nth-child(even){background-color: #f2f2f2}
</style>
</head>
<body>
<table>
<tr><th>ID</th><th>Lab1</th><th>Lab2</th></tr>
###table_body###
</table>
</body>
</html>"""
        self.assertEqual(expect, result)

    def test_generate_html_report(self):
        result = generate_html_report(lab_data)
        expect = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>
   Lab Marks
    </title>
    <style>
      table {
        border-collapse     : collapse;
        width               : 100%;
      }
      th, td {
        text-align          : left;
        padding             : 8px;
      }
      tr:nth-child(even) {
        background-color    : #f2f2f2
      }
    </style>
  </head>
  <body>
    <table>
      <tbody>
        <tr>
          <th>
            id/lab
          </th>
          <th>
            Lab01
          </th>
          <th>
            Lab02
          </th>
          <th>
            Lab03
          </th>
          <th>
            Lab04
          </th>
          <th>
            Lab05
          </th>
        </tr>
        <tr>
          <td>
            180031132
          </td>
          <td>
            0
          </td>
          <td>
            0
          </td>
          <td>
            0
          </td>
          <td>
            4
          </td>
          <td>
            5
          </td>
        </tr>
        <tr>
          <td>
            180074586
          </td>
          <td>
            12
          </td>
          <td>
            16
          </td>
          <td>
            6
          </td>
          <td>
            13
          </td>
          <td>
            9
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
"""
        self.assertEqual(normalize_line_endings(expect), normalize_line_endings(result))


if __name__ == '__main__':
    unittest.main()
