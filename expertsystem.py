import argparse
import re
import sys

sys.path.extend(["./parsing/"])

from Parser import Parser


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='path to input file.')

    return parser.parse_args()


def expertsystem():
    args = parse_args()
    expert = Parser(args.file)
    expert.eval_file()
    print(expert.rules, expert.facts, expert.queries)


if __name__ == "__main__":
    expertsystem()
