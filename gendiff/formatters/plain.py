def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    return f"'{value}'"


def walk(node, path=''):
    result = []
    for key, value in node.items():
        current_path = f"{path}{value['key']}"
        start_line = f"Property '{current_path}'"
        if value['operation'] == 'changed':
            result.append(f"{start_line} was updated. "
                          f"From {to_str(value['old'])} to {to_str(value['new'])}")
        if value['operation'] == 'nested':
            result.append(walk(value['value'], current_path + '.'))
        if value['operation'] == 'removed':
            result.append(f"{start_line} was removed")
        if value['operation'] == 'added':
            result.append(f"{start_line} was added "
                          f"with value: {to_str(value['value'])}")
    return '\n'.join(result)


def plain_format(diff_result: dict):
    return walk(diff_result)
