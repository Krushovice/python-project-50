from gendif.diff import generate_diff
# from gendif.parser import start_argparse


def main():
    diff = generate_diff('file_path1', 'file_path2')
    # args = start_argparse()
    print(diff)


if __name__ == '__main__':
    main()
