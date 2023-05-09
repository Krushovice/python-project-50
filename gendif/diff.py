import json


def check_format(array):
    for key in array:
        if array[key] is True:
            array[key] = 'true'
        elif array[key] is False:
            array[key] = 'false'
        elif array[key] is None:
            array[key] = 'null'
    return array


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    output = {}
    for key in json1.keys():
        output[key] = json1[key]

    for key in json2.keys():
        output[key] = json2[key]
    output = check_format(output)

    def to_string():
        sorted_keys = sorted(output.keys())
        my_list = ['{']
        for key in sorted_keys:
            value = output[key]
            if key in json1.keys():
                if key not in json2.keys():
                    my_list.append(f'- {key}: {value}')
            if key in json2.keys():
                if key not in json1.keys():
                    my_list.append(f'+ {key}: {value}')
            if key in json1.keys() & json2.keys():
                if json1[key] != json2[key]:
                    my_list.append(f'- {key}: {json1[key]}')
                    my_list.append(f'+ {key}: {json2[key]}')

                else:
                    my_list.append(f'{key}: {value}')
        my_list.append('}')

        result = "\n".join(my_list)

        return result
    return to_string()
