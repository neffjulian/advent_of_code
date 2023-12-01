from run_util import run_puzzle

import regex as re

NUMBERS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def part_a(data):
    return 0


def part_b(data):
    return 0


def main():
    examples = [
        ("""""", None, 281)
    ]
    day = int(__file__.split('/')[-1].split('.')[0][-2:])
    run_puzzle(day, part_a, part_b, examples)


if __name__ == '__main__':
    main()