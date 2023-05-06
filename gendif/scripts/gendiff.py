import argparse
import sys

sys.path.append('gendif/')


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


if __name__ == '__main__':
    from gendif import generate_diff
    print(generate_diff('gendif/file1.json', 'gendif/file2.json'))
