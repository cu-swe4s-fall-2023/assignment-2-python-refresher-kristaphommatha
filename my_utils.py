def get_column(file_name, query_column, query_value, result_column):
    result_list = []
    try:
        with open("file_name", "r") as file:
            for line in file:
                data = line.rstrip().split(',')
                if data[query_column] == str(query_value): #change query_value to string to match data[index] type
                    result_list.append(data[result_column])
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
                    
    return result_list
