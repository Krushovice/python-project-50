import pytest
import json
from tests import FIXTURES_PATH
from gendiff.formatters.stylish import build_line
from gendiff.formatters.formater import apply_format


@pytest.mark.parametrize("file, expected_path, format", [
    (
        f"{FIXTURES_PATH}/diff.txt",
        f"{FIXTURES_PATH}/expected_val_for_json.txt",
        'json'
    ),
    (
        f"{FIXTURES_PATH}/diff.txt",
        f"{FIXTURES_PATH}/expected_val_for_simple.txt",
        'plain'
    ),
    (
        f"{FIXTURES_PATH}/diff.txt",
        f"{FIXTURES_PATH}/expected_val_for_stylish.txt",
        'stylish'
    ),
])
def test_apply_format(file, expected_path, format):
    with open(expected_path, "r") as result, open(file, "r") as open_file:
        diff_file = json.load(open_file)
        apply_format(diff_file, format) == result.read()


def test_build_line():
    assert build_line({'key': 'verbose', 'any': 1},
                      'key', 1) == '    verbose: verbose'
