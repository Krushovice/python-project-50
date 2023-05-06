import argparse
import sys
import json

sys.path.append('gendif/')


parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.'
                    )
# Позиционные аргументы
parser.add_argument('first_file')
parser.add_argument('second_file')

# optional, именованные аргументы
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()
print(args)


if __name__ == '__main__':
    from gendif import generate_diff
    diff = generate_diff('modules/file1.json', 'modules/file2.json')
    print(json.dumps(diff, indent=2))
