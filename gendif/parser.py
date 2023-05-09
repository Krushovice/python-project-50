import argparse


def start_argparse():
    parser = argparse.ArgumentParser(
                        prog='gendiff',
                        description="""Compares two configuration
                        files and shows a difference."""
                        )
    # Позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # optional, именованные аргументы
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args
