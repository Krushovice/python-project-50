import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    output = {}
    for key in json1.keys():
        output[key] = json1[key]

    for key in json2.keys():
        output[key] = json2[key]

    def to_string():
        sorted_keys = sorted(output.keys())
        result = []
        for key in sorted_keys:
            value = output[key]
            if key in json1.keys():
                if key not in json2.keys():
                    result.append(f'- {key}: {value}')
            if key in json2.keys():
                if key not in json1.keys():
                    result.append(f'+ {key}: {value}')
            if key in json1.keys() & json2.keys():
                if json1[key] != json2[key]:
                    result.append(f'- {key}: {json1[key]}')
                    result.append(f'+ {key}: {json2[key]}')

                else:
                    result.append(f'{key}: {value}')
        return result

    return to_string()
