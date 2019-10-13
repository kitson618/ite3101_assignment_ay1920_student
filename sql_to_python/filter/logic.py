import os
import operator
from pathlib import Path
from typing import Dict, List


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
