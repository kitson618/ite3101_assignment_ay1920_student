import os
import operator
from pathlib import Path
from typing import Dict, List

from sql_to_python.file.file_helper import read_file


def is_test_passed(file_path_name: Path) -> bool:
    pass


def split_path(path: Path) -> List[str]:
    pass


def get_friendly_exercise_name(name: str) -> str:
    pass


def get_result_from_file(file_path_name: Path) -> Dict[str, str]:
    pass


def get_valid_and_invalid_exercise_lists(results: List[Dict[str, str]]) -> (List[Dict[str, str]], List[Dict[str, str]]):
    pass


def get_distinct_list(results: List[Dict[str, str]], key: str) -> List[str]:
    distinct = list(set(map(lambda x: x[key], results)))
    List.sort(distinct)
    return distinct

def get_sorted_list_singular(results: List[Dict[str,str]], key: str) -> List[Dict[str,str]]:
    results = sorted(results, key=lambda x: (x[key]))
    return results

def get_sorted_list(results: List[Dict[str,str]], *args: str) -> List[Dict[str,str]]:
    # allow multiple sort keys
    results = sorted(results, key=lambda x: ([x[key] for key in args]))
    return results

def generate_lab_mark(results: List[Dict[str, str]]) -> (List[str], List[List[str]]):
    headers = get_distinct_list(results, "lab")

    student_ids = get_distinct_list(results, "id")
    student_marks = []
    for student_id in student_ids:
        lab_marks = [student_id]
        for lab in headers:
            marks = len([x for x in results if x["id"] == student_id and x["lab"] == lab and x["status"] == "OK"])
            lab_marks.append(str(marks))
        student_marks.append(lab_marks)

    headers = ["id/lab"] + headers
    return headers, student_marks


def generate_data_list(results: List[Dict[str, str]]) -> (List[str], List[List[str]]):
    datalist, tmplist, header = [], [], []

    for row in results:
        for key in row:
            if results.index(row) == 0:
                header.append(key)
            tmplist.append(row[key])
        datalist.append(tmplist)
        tmplist = []

    return header, datalist
