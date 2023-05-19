import pytest
from gendif import generate_diff


@pytest.fixture()
def get_path():
    paths = {'json1': 'tests/fixtures/file1.json',
             'json2': 'tests/fixtures/file2.json',
             'yaml1': 'tests/fixtures/file1.yaml',
             'yaml2': 'tests/fixtures/file2.yaml',
    }
    return paths


@pytest.fixture()
def coll():
    with open('tests/fixtures/expected_value', 'r') as f:
        expected_value = f.read().strip()
        return expected_value


def test_output(coll, get_path):
    check_json = generate_diff(get_path['json1'], get_path['json2'])
    check_yaml = generate_diff(get_path['yaml1'], get_path['yaml2'])
    assert check_json == coll
    assert check_yaml == coll
