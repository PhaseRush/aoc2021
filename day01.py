import logging
from aocd import submit
from aocd.models import Puzzle

logging.basicConfig(level=logging.INFO)

puzzle = Puzzle(year=2021, day=1)
input = [int(line) for line in puzzle.input_data.splitlines()]


def part1():
    acc = 0
    for idx in range(1, len(input)):
        if input[idx] > input[idx - 1]:
            acc += 1
    logging.info(acc)
    submit(acc, part='a', day=1, year=2021)


def part2():
    m = []
    for i in range(0, len(input) // 3 * 3):
        m.append(input[i] + input[i + 1] + input[i + 2])

    acc = 0
    for i in range(1, len(m)):
        if m[i] > m[i - 1]:
            acc += 1
    logging.info(acc)
    submit(acc, part='b', day=1, year=2021)


if __name__ == '__main__':
    part1()
    part2()
