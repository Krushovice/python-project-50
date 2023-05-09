import json
from gendif.diff import generate_diff
from gendif.parser import start_argparse


def main():
    diff = generate_diff('gendif/file1.json', 'gendif/file2.json')
    print(start_argparse())
    print(json.dumps(diff, indent=2))


if __name__ == '__main__':
    main()
