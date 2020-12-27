from typing import Any

from aoc.day_01.core import part_1, part_2

sample_seed_1 = (1721, 979, 366, 299, 675, 1456)
sample_answer_1 = 514579
sample_answer_2 = 241861950


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 988771
    # assert part_2() == 0
    assert True


def verify_p1(data: Any, expected: Any) -> None:
    assert part_1(data) == expected


def verify_p2(data: Any, expected: Any) -> None:
    assert part_2(data) == expected


def test_p1() -> None:
    """"""
    examples = (
        (
            sample_seed_1,
            sample_answer_1,
        ),
    )

    for (data, expected) in examples:
        verify_p1(data, expected)


def test_p2() -> None:
    """"""
    examples = (
        (
            sample_seed_1,
            sample_answer_2,
        ),
    )

    for (data, expected) in examples:
        verify_p2(data, expected)
