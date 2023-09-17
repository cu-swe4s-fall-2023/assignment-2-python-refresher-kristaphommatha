[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher
## **This requires Agrofood_co2_emission.csv to be downloaded **
## run.sh
print.fire_py takes in 4 args and searches Agrofood_co2_emission.csv

./run.sh flag query_column query_value result_column

    flag can be 0 or 1

        input 1 if you want to specify a result_column, if 0 is input, the default is column 1
    
    query_column can be an integer
        
        this is the column you want to be searched
        
    query_value
        
        this is the value to search for in the query column
        
    result_column
    
        takes values from this column that are in the same row as query_value
        
This function will return an array of results from the result_column
