from gendif.scripts.gendiff import main


def check_output(func):
    assert main() == """{
    - follow: false
    host: hexlet.io
    - proxy: 123.234.53.22
    - timeout: 50
    + timeout: 20
    + verbose: true
    }"""
