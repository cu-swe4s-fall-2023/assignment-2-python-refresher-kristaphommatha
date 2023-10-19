[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher
## my_utils.py

    get_column(file_name, query_column, query_value, result_column)
    
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


## get_data.py

    get_data(file_name, query_column, query_value, result_column)
    
file_name == name of file to be parsed (string)

query_column == index of query column to search (int)

query_value == value to search for in query_column (int or string)

result_column == index of result column to grab info (int)

Calls get_column to parse through a data file. Stores the output from get_column into a newly generated .txt file that is named after query_value

## hist.py
    
    make_hist(data_file, out_file, title, xlabel, ylabel)
    
data_file == name of .txt generated from get_data.py,, argument *must include .txt*

out_file == desired name of output .png file,, argument *must include .png*

title == desired title of histogram to be generated

xlabel / ylabel == desired label for x-axis or y-axis, respectively

Reads properly formatted .txt file and generates a histogram from the data, stored in a new .png file


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

# v. 4 changes
## Continuous Integration
- Implemented continuous integration to run automatically run unit, functional, and style tests on future pushes and pull requests

# v. 5 changes
## Snakemake
- Added a Snakefile in data_presentation to gather data from Agrofood_co2_emission.csv available at https://docs.google.com/ucexport=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr and generate 3 histograms in a new folder titled pngs
### Histogram Discussion
*Introduction:* All 3 histograms plot frequency of Savanna fires in Afghanistan, Croatia, and Portugal over the last two decades. These three histograms can be found in data_presentations/pngs after running Snakemake.

*Results:* Overall, Croatia had the lowest frequency of Savanna fires, then Afghanistan, then Portugal. Both Croatia and Afghanistan tended to have 0 wilfires within one year, while Portugal tended to have 50 wildfires within one year. Afghanistan had some years where the amount of wildfires spiked up to 50 or 60. Croatia had up to 175 wildfires within 2 different years. 

*Methods:* Data was gathered using get_data.py found in src, which utilized get_columns and stored integer values into a new .txt file. After generating a .txt file with the desired data, hist.py was used to generate each histograms from the .txt files.

