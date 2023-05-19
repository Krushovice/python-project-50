from gendif.parser import parse_file


def check_format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def get_diff_entry(key, value1, value2):
    if value1 != value2:
        return [f'  - {key}: {value1}', f'  + {key}: {value2}']
    return [f'    {key}: {value1}']


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    output = {}
    for key in data1.keys():
        output[key] = check_format(data1[key])

    for key in data2.keys():
        if key not in output:
            output[key] = check_format(data2[key])

    sorted_keys = sorted(output.keys())
    result = ['{']
    for key in sorted_keys:
        if key in data1 and key in data2:
            result.extend(get_diff_entry(key, output[key], data2[key]))
        elif key in data1:
            result.append(f'  - {key}: {output[key]}')
        elif key in data2:
            result.append(f'  + {key}: {output[key]}')

    result.append('}')

    return '\n'.join(result)
