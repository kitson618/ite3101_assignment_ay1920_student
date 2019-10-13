from pathlib import Path
from typing import List, Dict

from sql_to_python.excel.tool import read_excel, read_excel_dataframes, create_spreadsheet, generate_excel
from sql_to_python.excel.tool import write_excel
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list

from openpyxl import load_workbook
import pandas as pd


# Question 1
# SQL: SELECT * FROM Emp;
def query_all(file_path_name: Path, sheet_name: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    # export to output excel
    write_excel(results, 'Q1')


# Question 2
# SQL: SELECT ename, hiredate
# 	FROM Emp
# 	WHERE hiredate LIKE '01-MAY%';
def query_with_filter(file_path_name: Path, sheet_name: str):
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []
    for row in results:
        for key in row:
            if "05-01" in row[key]:
                results_tmp.append(row)
    results = results_tmp
    write_excel(results, 'Q2')


# Question 3
# SQL: SELECT empNo, mgr
# 	FROM Emp
# 	ORDER BY empNo ASC;
def query_with_order(file_path_name: Path, sheet_name: str, select_f1: str, select_f2: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}

    for row in results:
        for key in row:
            if key == select_f1 or key == select_f2:
                dict_tmp.update({key:row[key]})
        else:
            results_tmp.append(dict_tmp)
        dict_tmp = {}

    results_tmp = get_sorted_list(results_tmp,select_f1)
    results = results_tmp

    # export to output excel
    write_excel(results, 'Q3')


# Question 4
# DELETE Emp
# 	WHERE eName = 'MARTIN';
def delete_record_query(file_path_name: Path, sheet_name: str, delete_f: str, delete_v: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []

    for row in results:
        for key in row:
            if key == delete_f and row[key] == delete_v:
                break
        else:
            results_tmp.append(row)

    results = results_tmp

    # export to output excel
    write_excel(results, 'Q4')



# Question 5
# SQL:
# (1) UPDATE Emp
# 	SET salary = 60000
# 	WHERE empNo =7839;
def update_record_query(file_path_name: Path, sheet_name: str, update_f: str, \
                        update_v: int, filter_f: str, filter_v: int):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []

    for row in results:
        for key in row:
            if key == filter_f and row[key] == str(filter_v):
                row[update_f] = str(update_v)
        results_tmp.append(row)

    results = results_tmp

    # export to output excel
    write_excel(results, 'Q5')


# Question 6
# SQL:
# (1) ALTER TABLE Salgrade ADD diff NUMBER DEFAULT hiSal - loSal;
# (2) SELECT * FROM Salgrade;
# => with computed value (diff = hiSal - loSal)
def add_table_column_query(file_path_name: Path, sheet_name: str, new_f: str, \
                           source_f_1: str, source_f_2: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}
    v1 = v2 = 0

    for row in results:
        for key in row:
            dict_tmp.update({key:row[key]})
            if(key==source_f_1):
                v1 = int(row[source_f_1])
            elif(key==source_f_2):
                v2 = int(row[source_f_2])
        else:
            dict_tmp.update({new_f:str(abs(v1-v2))})
        results_tmp.append(dict_tmp)
        dict_tmp = {}

    results = results_tmp

    # export to output excel
    write_excel(results, 'Q6')


# Question 7
# SQL: SELECT deptNo, COUNT(empNo)
# 	FROM Emp
# 	WHERE job = 'CLERK'
# 	GROUP BY deptNo;
def query_with_groupby(file_path_name: Path, sheet_name: str, groupby_f: str, \
                       count_f: str, filter_f: str, filter_v: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_tmp = []
    dict_tmp = {}
    count = 0

    gropby_list = get_distinct_list(results, groupby_f)

    #read loop
    for group in gropby_list:
        for row in results:
            for key in row:
                if row[key] == group and row[filter_f] == filter_v:
                    count += 1
        if count != 0:
            dict_tmp.update({groupby_f: group})
            dict_tmp.update({"COUNT(" + count_f + ")": str(count)})
            results_tmp.append(dict_tmp)
            dict_tmp = {}
            count = 0

    results = results_tmp
    # export to output excel
    write_excel(results, 'Q7')


# Question 8
# SQL: SELECT Sup.empNo AS "Supervisor", Sup.eName AS "SupName",
# 		Sub.empNo AS "Subordinate", Sub.eName AS "SubName"
# 	    FROM Emp Sup, Emp Sub
# 	    WHERE Sup.empNo = Sub.mgr
def query_multiple_tables_A(file_path_name: Path, sheet_name: str, filter_f_1: str, \
                            filter_f_2: str, select_f_1: str, select_f_2: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_duplicate = results
    results_tmp = []
    dict_tmp = {}

    join_list = get_distinct_list(results, filter_f_1)

    for row in results_duplicate:
        for key in row:
            if key == filter_f_2 and row[filter_f_2] in join_list:
                i = row[filter_f_2]
                v1 = [d[select_f_1] for d in results if d[select_f_1] == i].pop()
                v2 = [d[select_f_2] for d in results if d[select_f_1] == i].pop()
                dict_tmp.update({"Parent":v1})
                dict_tmp.update({"PName":v2})
                dict_tmp.update({"Child":row[select_f_1]})
                dict_tmp.update({"CName":row[select_f_2]})
                results_tmp.append(dict_tmp)
                dict_tmp = {}

    results = get_sorted_list(results_tmp,"Parent","Child")

    # export to output excel
    write_excel(results, 'Q8')



# Question 9
# SQL:
# 	SELECT e1.empNo, e1.eName, e1.salary, e2.empNo, e2.eName, e2.salary
# 	FROM Emp e1, Emp e2
# 	WHERE e1.salary = e2.salary AND e1.empNo < e2.empNo;
def query_multiple_tables_B(file_path_name: Path, sheet_name: str, filter_f_1: str, \
                            filter_f_2: str, select_f_1: str, select_f_2: str, select_f_3: str):
    # get source data set
    results = read_excel(file_path_name, sheet_name)
    results_duplicate = results
    results_tmp = []
    dict_tmp = {}

    join_list = get_distinct_list(results, filter_f_1)

    for row in results_duplicate:
        if row[filter_f_1] in join_list:
            i = row[filter_f_1]
            v_list = [d[select_f_1] for d in results if d[filter_f_1] == i and d[select_f_1] < row[select_f_1]]
            for v in v_list:
                dict_tmp.update({"P1"+select_f_1:v})
                dict_tmp.update({"P1"+select_f_2:d[select_f_2] for d in results if d[filter_f_2] == v})
                dict_tmp.update({"P1"+select_f_3:d[select_f_3] for d in results if d[filter_f_2] == v})
                dict_tmp.update({"P2"+select_f_1:row[select_f_1]})
                dict_tmp.update({"P2"+select_f_2:row[select_f_2]})
                dict_tmp.update({"P2"+select_f_3:row[select_f_3]})
                results_tmp.append(dict_tmp)
                dict_tmp = {}

    results = get_sorted_list(results_tmp,"P1"+select_f_1,"P2"+select_f_2)

    print(results)

    # export to output excel
    write_excel(results, 'Q9')


# Question 10
# SQL:
# CREATE TABLE Publisher (
# 	publisherID		CHAR(2)			NOT NULL,
# 	publisherName	VARCHAR2(50) 		NOT NULL,
# 	address		VARCHAR2(250) 		NULL,
# 	CONSTRAINT 	publisher_pk 			PRIMARY KEY (publisherID)
# );
#
# INSERT INTO Publisher VALUES ('NE', 'New 2000 Publishing', 'Hong Kong');
# INSERT INTO Publisher VALUES ('SA', 'South Asia Limited', 'Singapore');
# INSERT INTO Publisher VALUES ('OR', 'Oriental Publishing', 'Taiwan');
def create_table(file_path_name: Path, sheet_name: str):
    # get source data set
    results = [
                {"publisherID":"NE","publisherName":"New 2000 Publishing","address":"Hong Kong"},
                {"publisherID":"SA","publisherName":"South Asia Limited","address":"Singapore"},
                {"publisherID":"OR","publisherName":"Oriental Publishing","address":"Taiwan"},
              ]

    # export to output excel
    write_excel(results, sheet_name)


# test_data
file = Path("../../data/source_data.xlsx")
generate_excel()
query_all(file, "Emp")
query_with_filter(file, "Emp")
query_with_order(file, "Emp", "empNo", "mgr")
delete_record_query(file,"Emp", "eName", "MARTIN")
update_record_query(file,"Emp","salary",60000,"empNo",7839)
add_table_column_query(file,"Salgrade","diff","hiSal","loSal")
query_with_groupby(file,"Emp","deptNo","empNo","job","CLERK")
query_multiple_tables_A(file,"Emp","empNo","mgr","empNo","eName")
query_multiple_tables_B(file,"Emp","salary","empNo","empNo","eName","salary")
create_table(file,"Publisher")



# wb = load_workbook(filename=file)
# sheet_ranges = wb['Emp']
# df = pd.DataFrame(sheet_ranges.values)
# print(df)
