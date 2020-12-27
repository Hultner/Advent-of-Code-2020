from typing import Any

from aoc.day_02.core import part_1, part_2

sample_seed_1 = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""
answer_1 = 2
answer_2 = 1


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 515
    assert part_2() == 711
    assert True


def verify_p1(data: Any, expected_1: Any, expected_2: Any) -> None:
    assert part_1(data) == expected_1
    assert part_2(data) == expected_2


def test_p1() -> None:
    """"""
    examples = ((sample_seed_1, answer_1, answer_2),)

    for (data, expected_1, expected_2) in examples:
        verify_p1(data, expected_1, expected_2)
