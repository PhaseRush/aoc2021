import logging
from aocd import submit
from aocd.models import Puzzle
logging.basicConfig(level=logging.INFO)

DAY =


puzzle = Puzzle(year=2021, day=DAY)
input = [line.split() for line in puzzle.input_data.splitlines()]


def part1():
    logging.info()
    submit(, part='a', day=DAY, year=2021)


def part2():

    logging.info()
    submit(, part='b', day=DAY, year=2021)


if __name__ == '__main__':
    part1()
    part2()
