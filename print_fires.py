import my_utils as utils
import argparse
import sys

def main():

    try:
        parser = argparse.ArgumentParser(description='Searches through a file '
                                                     ' given a query column,'
                                                     ' query value, and result'
                                                     ' columns and outputs the'
                                                     'values in the result'
                                                     ' column as integers',
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
                            nargs='?',
                            const=1,
                            default=3)

        args = parser.parse_args()
    except Exception as e:
        print('Invalid input')
        return

    try:
        fires = utils.get_column(args.file_name, args.qc, args.qv, args.rc)
    except FileNotFoundError:
        print('Could not find ' + args.file_name + ' in current directory.')
        sys.exit(1)
    except PermissionError:
        print('Can not read ' + args.file_name + '.')
        sys.exit(2)
    except IndexError:
        print('Query Column or Result Column input exceeds columns in file.')
        sys.exit(3)
    except Exception as e:
        print('An unknown error occured.')
        sys.exit(4)

    print(fires)


if __name__ == '__main__':

    main()
