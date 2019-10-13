import os
import shutil
import zipfile
from pathlib import Path
from typing import List


def unzip_to_folder(source_zip: Path, target_dir: Path):
    zip_file = zipfile.ZipFile(str(source_zip.absolute()))
    zip_file.extractall(str(target_dir.absolute()))
    zip_file.close()


def delete_folder(target_dir: Path):
    shutil.rmtree(str(target_dir))


def read_file(file_path_name: Path) -> str:
    with open(str(file_path_name), 'r') as file:
        return file.read()


def list_all_files(path: Path) -> List[Path]:
    file_name_list = []
    for root, d_names, f_names in os.walk(str(path)):
        for f in f_names:
            file_name_list.append(Path(f))
    file_name_list.sort()
    return file_name_list


def save_to_file(file_path_name: Path, content: str):
    with open(str(file_path_name), "w") as text_file:
        print(content, file=text_file)