from pathlib import Path
from typing import List, Dict

import pandas as pd
from sql_to_python.filter.logic import get_sorted_list, get_distinct_list
from sql_to_python.translator.translator import read_source_excel


# Question 10
# SQL:
# CREATE TABLE Publisher (
# 	publisherID		CHAR(2)			NOT NULL,
# 	publisherName	VARCHAR2(50) 		NOT NULL,
# 	address		    VARCHAR2(250) 		NULL,
# 	CONSTRAINT 	    publisher_pk 		PRIMARY KEY (publisherID)
# );
#
# INSERT INTO Publisher VALUES ('NE', 'New 2000 Publishing', 'Hong Kong');
# INSERT INTO Publisher VALUES ('SA', 'South Asia Limited', 'Singapore');
# INSERT INTO Publisher VALUES ('OR', 'Oriental Publishing', 'Taiwan');
def create_table(file_path_name: Path) -> List[Dict[str,str]]:

    pass

    # export to output excel
