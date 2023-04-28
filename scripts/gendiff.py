import argparse
import json
from files import file1, file2

parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.'
                    )
# Позиционные аргументы
parser.add_argument('first_file', type=argparse.FileType('w'))
parser.add_argument('second_file', type=argparse.FileType('w'))

# optional, именованные аргументы
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()
print(args)


def generate_diff(file_path1, file_path2):
    pass


if __name__ == '__main__':
    generate_diff(file1, file2)
