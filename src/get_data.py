import my_utils as utils
import argparse
import sys


def get_data(file_name, qc, qv, rc):
    try:
        data = utils.get_column(file_name, qc, qv, rc)
    except FileNotFoundError:
        return -1
    except PermissionError:
        return -2
    except IndexError:
        return -3
    except Exception as e:
        return None

    dataString = [str(i) for i in data]
    toWrite = "\n".join(dataString)

    newFile = "../data_presentations/txts/" + qv + ".txt"

    with open(newFile, "w") as file:
        file.write(toWrite)
    return 1


def main():
    try:
        parser = argparse.ArgumentParser(description='Searches through a file '
                                                     ' given a query column,'
                                                     ' query value, and result'
                                                     ' columns and outputs the'
                                                     ' values in a new .txt'
                                                     ' file named after qv',
                                         prog='get_columns')

        parser.add_argument('--file_name',
                            type=str,
                            help='Input name of file to parse',
                            required=True)

        parser.add_argument('--qc',
                            type=int,
                            help='Index of query column to search, starting'
                                 ' from index 1',
                            required=True)

        parser.add_argument('--qv',
                            type=str,
                            help='Value to search for in query column',
                            required=True)

        parser.add_argument('--rc',
                            type=int,
                            help='Index of result column to search, starting'
                                 ' from index 1',
                            required=True)
        args = parser.parse_args()

    except Exception as e:
        print('Invalid input')
        return

    result = get_data(args.file_name, args.qc, args.qv, args.rc)
    if result == -1:
        print('Could not find ' + args.file_name + ' in current directory.')
        sys.exit(1)
    if result == -2:
        print('Can not read ' + args.file_name + '.')
        sys.exit(2)
    if result == -3:
        print('Query Column or Result Column input exceeds columns in file.')
        sys.exit(3)
    if result is None:
        print('An unknown error occured.')
        sys.exit(4)


if __name__ == '__main__':
    main()
