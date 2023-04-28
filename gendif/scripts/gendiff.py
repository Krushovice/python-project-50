import argparse
import json

# parser = argparse.ArgumentParser(
#                     prog='gendiff',
#                     description='Compares two configuration files and shows a difference.'
#                     )
# # Позиционные аргументы
# parser.add_argument('first_file', type=argparse.FileType('w'))
# parser.add_argument('second_file', type=argparse.FileType('w'))

# # optional, именованные аргументы
# parser.add_argument('-f', '--format', help='set format of output')

# args = parser.parse_args()
# print(args)


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file_1:
        data1 = json.load(file_1)
    with open(file_path2, 'r', encoding='utf-8') as file_2:
        data2 = json.load(file_2)


if __name__ == '__main__':
    print(generate_diff('gendif/file1.json', 'gendif/file2.json'))
