import pytest
from gendif import generate_diff


@pytest.fixture()
def get_path():
    paths = {'json1': 'tests/fixtures/file1.json',
             'json2': 'tests/fixtures/file2.json',

    }
    return paths


@pytest.fixture()
def coll():
    with open('tests/fixtures/expected_value', 'r') as f:
        expected_value = f.read()
        return expected_value


def test_output(coll, get_path):
    result = generate_diff(get_path['json1'], get_path['json2'])
    assert result == coll
