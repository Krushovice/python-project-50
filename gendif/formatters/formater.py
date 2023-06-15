from gendif.formatters.stylish import stylish_format
from gendif.formatters.simple import set_format
from gendif.formatters.json import json_format


def apply_format(diff_result, format):
    if format == 'stylish':
        return stylish_format(diff_result)
    if format == 'simple':
        return set_format(diff_result)
    if format == 'json':
        return json_format(diff_result)
    raise Exception(f"You chose the wrong format!: {format}")
