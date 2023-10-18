import my_utils as utils
import argparse
import sys
import matplotlib
matplotlib.use('Agg')  # noqa
import matplotlib.pyplot as plt


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


def main():
    try:
        parser = argparse.ArgumentParser(description='Generates a .png'
                                                     ' histogram from data'
                                                     ' in a .txt file',
                                         prog='get_columns')

        parser.add_argument('--file_name',
                            type=str,
                            help='.txt file containing data',
                            required=True)

        parser.add_argument('--out_name',
                            type=str,
                            help='Name of .png to output',
                            required=True)

        parser.add_argument('--t',
                            type=str,
                            help='Title of historgram',
                            required=True)

        parser.add_argument('--x',
                            type=str,
                            help='x-axis label',
                            required=True)

        parser.add_argument('--y',
                            type=str,
                            help='y-axis label',
                            nargs='?',
                            default='Frequency')
        args = parser.parse_args()

    except Exception as e:
        print('Invalid input')
        return

    result = make_hist("../data_presentations/txts/" + args.file_name, "../data_presentations/pngs/" + args.out_name, args.t, args.x, args.y)
    if result == -1:
        print(args.file_name + " does not exist")
        sys.exit(1)
    if result == -2:
        print("Could not access " + args.file_name)
        sys.exit(2)
    if result is None:
        print("Unknown error")
        sys.exit(3)


if __name__ == '__main__':
    main()
