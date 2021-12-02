import logging

from aocd import submit
from aocd.models import Puzzle

logging.basicConfig(level=logging.INFO)
puzzle = Puzzle(year=2021, day=2)
input = [line.split() for line in puzzle.input_data.splitlines()]
input = [(tuple[0], int(tuple[1])) for tuple in input]


def part1():
    depth = 0
    horizontal = 0

    for command in input:
        match command:
            case ["forward", int(o)]:
                horizontal += o
            case ["down", int(o)]:
                depth += o
            case ["up", int(o)]:
                depth -= o


    logging.info(depth * horizontal)
    submit(depth * horizontal, part='a', day=2, year=2021)


def part2():
    depth = 0
    horizontal = 0
    aim = 0

    for command in input:
        match command:
            case ["forward", int(o)]:
                horizontal += o
                depth += aim * o
            case ["down", int(o)]:
                aim += o
            case ["up", int(o)]:
                aim -= o

    logging.info(depth * horizontal)
    submit(depth * horizontal, part='b', day=2, year=2021)


if __name__ == '__main__':
    part1()
    part2()
