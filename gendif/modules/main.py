import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r', encoding='utf-8') as file_1:
        data1 = json.load(file_1)
    with open(file_path2, 'r', encoding='utf-8') as file_2:
        data2 = json.load(file_2)

    difference = (set(data1) - set(data2))
    intersect = (set(data1) & set(data2))
    list_of_dif = []
    for k in difference:
        list_of_dif.append(k)
    list_of_inter = []
    for k in intersect:
        list_of_inter.append(k)

    return f"""
            - {list_of_dif[0]}: {data1[list_of_dif[0]]}
            - {list_of_dif[1]}: {data1[list_of_dif[1]]}
            + {list_of_inter[0]}: {data1[list_of_inter[0]]}
            + {list_of_inter[1]}: {data1[list_of_inter[1]]}
    """


print(generate_diff('gendif/file1.json', 'gendif/file2.json'))
