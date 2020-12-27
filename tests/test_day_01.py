from typing import Any
from aoc.day_01.core import (
    part_1,
    part_2,
)

sample_seed = (1721, 979, 366, 299, 675, 1456)
sample_answer = 514579


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 988771
    # assert part_2() == 0
    assert True


def verify_p1(data: Any, expected: Any) -> None:
    # breakpoint()
    assert part_1(data) == expected


def test_p1() -> None:
    """"""
    examples = ((sample_seed, sample_answer,),)

    for (data, expected) in examples:
        verify_p1(data, expected)
