import json


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    output = {}
    for key in json1.keys():
        if key not in json2:
            output[key] = {
                '- ' + key: json1[key]
            }

    for key in json2.keys():
        if key not in json1:
            output[key] = {
                '+ ' + key: json2[key]
            }

    for key in json1.keys() & json2.keys():
        if json1[key] != json2[key]:
            output[key] = {
                '- ' + key: json1[key],
                '+ ' + key: json2[key]
            }
        else:
            output[key] = {
                key: json1[key]
            }
    return output
