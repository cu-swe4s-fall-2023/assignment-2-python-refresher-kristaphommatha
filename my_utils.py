def get_column(file_name, query_column, query_value, result_column=3):
    result_list = []

    with open(file_name, "r") as file:
        for line in file:
            data = line.rstrip().split(',')
            if data[query_column-1] == str(query_value):
                # change query_value to string to match data[index] type
                float_convert = float((data[result_column-1]))
                # converts str to float first bec of decimal values
                result_list.append(int(float_convert))
    return result_list
