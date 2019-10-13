headers = ["ID", "Lab1", "Lab2"]

marks = [["123456789", "12", "13"], ["987654321", "22", "23"]]

lab_data = [{'id': '180031132', 'lab': 'Lab04', 'exercise': 'Task 14 Elif', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab04', 'exercise': 'Task 09 This N That', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab04', 'exercise': 'Task 12 If Having', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab04', 'exercise': 'Task 15 Big If', 'status': 'Failed'},
            {'id': '180031132', 'lab': 'Lab04', 'exercise': 'Task 10 Mix N Match', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 01 Ahoy', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 04 Check Yourself More', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 02 Input', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 08 Move It Back', 'status': 'OK'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 09 Ending Up', 'status': 'Failed'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 03 Check Yourself', 'status': 'Failed'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 07 Word Up', 'status': 'Failed'},
            {'id': '180031132', 'lab': 'Lab05', 'exercise': 'Task 06 Ay B C', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 13 Explicit String Conversion', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 03 Escaping Characters', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 05 String Methods', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 01 Strings', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 12 String Concatenation', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 08 Str', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 06 Lower', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 15 String Formatting With Percentage 2',
             'status': 'OK'}, {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 02 Practice', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 16 Sth Completely Familiar', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 07 Upper', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 14 String Formatting With Percentage 1',
             'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 11 Printing Variables', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 04 Access By Index', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 09 Dot Notation', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab02', 'exercise': 'Task 10 Printing Strings', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 03 Extracting Info', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 02 Get Current Date Time', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 05 Pretty Time', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 06 Grand Finale', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 04 Hot Date', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab03', 'exercise': 'Task 01 The Datetime Library', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 02 Print Statements', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 08 Comments', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 01 Hello World', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 11 Multi Line Strings', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 05 Variables', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 06 Arithmetic', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 04 Handling Errors', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 03 Strings', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 13 Value Error', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 07 Updating Variables', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 09 Numbers', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab01', 'exercise': 'Task 10 Two Types Of Division', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 02 Compare Closely', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 03 Compare Closelier', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 13 Else', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 14 Elif', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 08 Not', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 09 This N That', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 04 How Tables Have Turned', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 12 If Having', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 06 And', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 07 Or', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 15 Big If', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 10 Mix N Match', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab04', 'exercise': 'Task 11 Con Statement Syntax', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 01 Ahoy', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 04 Check Yourself More', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 02 Input', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 08 Move It Back', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 09 Ending Up', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 03 Check Yourself', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 10 Test', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 07 Word Up', 'status': 'OK'},
            {'id': '180074586', 'lab': 'Lab05', 'exercise': 'Task 06 Ay B C', 'status': 'OK'}
            ]