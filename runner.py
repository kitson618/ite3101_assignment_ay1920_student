from pathlib import Path

from sql_to_python.result.result_generator import generate_result

if __name__ == '__main__':
    generate_result(Path("data/source_data.zip"), Path("out/"))
