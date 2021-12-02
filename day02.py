import logging

from aocd import submit
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=2)
input = [line.split() for line in puzzle.input_data.splitlines()]
input = [(tuple[0], int(tuple[1])) for tuple in input]


def part1():
    depth = 0
    horizontal = 0

    for command in input:
        if command[0] == "forward":
            horizontal += command[1]
        elif command[0] == "down":
            depth += command[1]
        else:
            depth -= command[1]

    logging.info(depth * horizontal)
    submit(depth * horizontal, part='a', day=2, year=2021)


def part2():
    depth = 0
    horizontal = 0
    aim = 0

    for command in input:
        if command[0] == "forward":
            horizontal += command[1]
            depth += aim * command[1]
        elif command[0] == "down":
            aim += command[1]
        else:
            aim -= command[1]

    logging.info(depth * horizontal)
    submit(depth * horizontal, part='b', day=2, year=2021)


if __name__ == '__main__':
    part1()
    part2()
