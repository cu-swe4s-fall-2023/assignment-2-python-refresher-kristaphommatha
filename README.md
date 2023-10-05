[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher
## my_utils.py

    get_column(file_name, query_column, query_value, and result_column)
    
file_name == name of file to be parsed (string)

query_column == index of query column to search (int)

query_value == value to search for in query_column (int or string)

result_column == index of result column to grab info (int)

Parses through a file line by line and searches the query column index for a query value. Once found, it will store the value in the corresponding result_column. Returns an list of values from result_column as rounded-down integers.

    get_mean(ints)
    
ints == list of integers

Returns mean of list

    get_median(ints)
ints == list of integers

Returns median of list    

    get_stdev(ints)
ints == list of integers

Returns standard deviation of list  
    


## print_fires.py

Takes user input for file name as --file_name, query column as --qc, query value as --qv, result column as --rc, and statistical operation as --op.

--rc and --op are optional. --rc is defaulted to 3 if no argument is input and --op is not performed if no argument is input.
--op is only valid for 3 inputs: mean, median, or stdev

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

# v.3 changes
## Implementing Statistical Functions
- Implemented functions in my_utils.py to find the mean, median, or standard deviation of a list of integers

## Functionality changes
- Updated print_fires.py to take in an additional optional argument that lets the user decide what statistical operation to perform on their output list

## Unit testing and functional testing
- Added unit tests to test mean, median, and mode functions
- Added functional tests to test the expected outputs of print_fires.py

