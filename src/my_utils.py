import math


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


def get_mean(ints):
    csum = 0
    for i in range(len(ints)):
        csum += i
    mean = csum / len(ints)
    return mean


def get_median(ints):
    middle = len(ints) / 2
    if len(ints) % 2 == 0:
        med = (ints[middle - 1] + ints[middle]) / 2
    else:
        med = ints[middle]
    return med


def get_stdev(ints):
    mean = get_mean(ints)
    diffSum = 0
    for i in range(len(ints)):
        diffSum += (mean - ints[i])**2
    stdev = math.sqrt(diffSum / len(ints))
    return stdev
