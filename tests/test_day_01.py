from typing import  Any
from aoc.day_XX.core import (
    part_1,
    part_2,
)


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 0
    assert part_2() == 0
    assert True


def verify_x(data: Any, expected: Any) -> None:
    assert True


def test_x() -> None:
    """"""
    examples = ((0, 1),)

    for (data, expected) in examples:
        verify_x(data, expected)
