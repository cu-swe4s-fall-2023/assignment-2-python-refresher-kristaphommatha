import my_utils as utils
import argparse
import sys


def get_data(file_name, qc, qv, rc):
    data = utils.get_column(file_name, qc, qv, rc)

    dataString = [str(i) for i in data]
    toWrite = "\n".join(dataString)

    newFile = qv + ".txt"

    with open(newFile, "w") as file:
        file.write(toWrite)


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

    get_data(args.file_name, args.qc, args.qv, args.rc)


if __name__ == '__main__':
    main()
