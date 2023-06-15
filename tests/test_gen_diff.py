from gendiff import generate_diff
from tests import FIXTURES_PATH
import pytest


@pytest.mark.parametrize("file1, file2, expected_path, format", [
    (
        f"{FIXTURES_PATH}/example_file1.json",
        f"{FIXTURES_PATH}/example_file2.json",
        f"{FIXTURES_PATH}/expected_val_for_example.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1_example.yml",
        f"{FIXTURES_PATH}/file2_example.yml",
        f"{FIXTURES_PATH}/expected_val_for_example.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/expected_val_for_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/expected_val_for_simple.txt",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/file1.json",
        f"{FIXTURES_PATH}/file2.json",
        f"{FIXTURES_PATH}/expected_val_for_json.txt",
        "json"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/expected_val_for_stylish.txt",
        "stylish"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/expected_val_for_simple.txt",
        "plain"
    ),
    (
        f"{FIXTURES_PATH}/file1.yml",
        f"{FIXTURES_PATH}/file2.yml",
        f"{FIXTURES_PATH}/expected_val_for_json.txt",
        "json"
    ),
])
def test_generate_diff(file1, file2, expected_path, format):
    with open(expected_path, "r") as result:
        assert result.read() == generate_diff(file1, file2, format)
