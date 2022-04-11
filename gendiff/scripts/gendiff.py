import argparse
from sqlite3 import paramstyle


def main():
    pharser = argparse.ArgumentParser(description="Generate diff")
    pharser.add_argument("first_file")
    pharser.add_argument("second_file")
    pharser.add_argument("-f", "--format")
    pharser.parse_args()


if __name__ == "__main__":
    main()
