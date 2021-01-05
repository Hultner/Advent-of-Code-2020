from typing import Any

from aoc.day_03.core import part_1, part_2

sample_seed_1 = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".strip()

answers = [7, 336,]

def test_parts() -> None:
    # Oracle says so
    assert part_1() == 292
    assert part_2() == 9354744432
    assert True


def verify_x(data: Any, expected_1: Any, expected_2: Any) -> None:
    assert part_1(data) == expected_1
    assert part_2(data) == expected_2


def test_x() -> None:
    """"""
    examples = ((sample_seed_1, answers),)

    for (data, expected) in examples:
        verify_x(data, *expected)
