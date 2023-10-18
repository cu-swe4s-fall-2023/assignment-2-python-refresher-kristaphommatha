import math
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


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
    cSum = 0
    try:
        for i in ints:
            cSum += i
    except Exception as e:
        return None
    try:
        mean = cSum / len(ints)
    except Exception as e:
        return None
    return mean


def get_median(ints):
    sortedInts = sorted(ints)
    middle = int(len(ints) / 2)
    try:
        if len(ints) % 2 == 0:
            med = (sortedInts[middle - 1] + sortedInts[middle]) / 2
        else:
            med = sortedInts[middle]
    except Exception as e:
        return None

    return med


def get_stdev(ints):
    mean = get_mean(ints)
    diffSum = 0
    try:
        for i in ints:
            diffSum += (mean - i)**2
    except TypeError:
        return None
    except Exception as e:
        return None
    try:
        stdev = math.sqrt(diffSum / len(ints))
    except Exception as e:
        return None
    return stdev


def make_hist(data_file, out_file, title, x, y):
    D = []
    try:
        for line in open(data_file):
            D.append(float(line))
    except FileNotFoundError:
        return -1
    except PermissionError:
        return -2
    except Exception as e:
        return None

    fig, ax = plt.subplots()
    ax.hist(D)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)

    plt.savefig(out_file, bbox_inches='tight')
    return 1
