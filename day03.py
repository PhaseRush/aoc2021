import logging
from typing import List

from aocd import submit
from aocd.models import Puzzle
logging.basicConfig(level=logging.INFO)

DAY = 3
puzzle = Puzzle(year=2021, day=DAY)
input = puzzle.input_data.splitlines()


def join(l: List[int]) -> int:
    l = ['1' if int(x) > 0 else '0' for x in l]
    l = ''.join(l)
    return int(l, 2)


def part1():
    freq = [0] * len(input[0])
    max = join([1] * len(input[0]))
    for num in input:
        for idx in range(0, len(num)):
            if num[idx] == '1':
                freq[idx] += 1
            else:
                freq[idx] -= 1

    gamma = join(freq)
    epsilon = max - gamma

    submit(gamma * epsilon, part='a', day=DAY, year=2021)


def histo(candidates: List[str], one_greater: str, zero_greater: str) -> int:
    for idx in range(len(input[0])):
        if len(candidates) == 1:
            break
        num0 = len(candidates) - (num1 := sum(num[idx] == '1' for num in candidates))
        if num1 >= num0:
            candidates = [num for num in candidates if num[idx] == one_greater]
        else:
            candidates = [num for num in candidates if num[idx] == zero_greater]

    return int(candidates[0], 2)


def part2():
    oxy = histo(input.copy(), '0', '1')
    co2 = histo(input.copy(), '1', '0')

    logging.info(oxy * co2)
    submit(oxy * co2, part='b', day=DAY, year=2021)


if __name__ == '__main__':
    part1()
    part2()
