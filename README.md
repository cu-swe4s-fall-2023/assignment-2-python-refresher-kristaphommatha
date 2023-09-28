[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher
## my_utils.py

    Contains get_column(file_name, query_column, query_value, and result_column) function
    
file_name == name of file to be parsed (string)

query_column == index of query column to search (int)

query_value == value to search for in query_column (int or string)

result_column == index of result column to grab info (int)


This function parses through a file ;ine by line and searches the query column index for a query value. Once found, it will store the value in the corresponding result_column. Returns an array of values from result_column as rounded-down integers.

## print_fires.py

Takes user input for file name as --file_name, query column as --qc, query value as --qv, and result column as --rc. The result column argument is optional and defaulted to 3.

## run.sh

Runs 3 test cases: 1 successful case, 1 case with a file that does not exist, and 1 case with an input that exceeds the number of columns in the file.

# v.2 changes
## Best Practices changes
- Updated python files to follow pep8 style guide
- Implemented system exit codes to indicate error
- Implemented main function in print_fires.py to call math_lib.py functions
- Updated print_fires.py to take in user arguments using argparse

## Functionality changes
- Updated get_columns function to return a list of integers
- Added input validation into print_fires.py
