import json
import sys

sys.path.append('gendif/')


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    output = {}
    # Check for keys present in file1 but not in file2
    for key in json1.keys():
        if key not in json2:
            output[key] = {
                '- ' + key: json1[key]
            }

    # Check for keys present in file2 but not in file1
    for key in json2.keys():
        if key not in json1:
            output[key] = {
                '+ ' + key: json2[key]
            }

    # Check for keys with different values
    for key in json1.keys() & json2.keys():
        if json1[key] != json2[key]:
            output[key] = {
                '- ' + key: json1[key],
                '+ ' + key: json2[key]
            }

    return output


file1 = 'file1.json'
file2 = 'file2.json'
output = generate_diff(file1, file2)
print(json.dumps(output, indent=2))

# print(generate_diff('gendif/file1.json', 'gendif/file2.json'))
