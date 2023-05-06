import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file_1:
        data1 = json.load(file_1)
    with open(file_path2, 'r', encoding='utf-8') as file_2:
        data2 = json.load(file_2)
    return 'hello'







# print(generate_diff('gendif/file1.json', 'gendif/file2.json'))
