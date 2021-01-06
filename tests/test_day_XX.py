from typing import Any

from aoc.day_XX.core import part_1, part_2

sample_seed_1 = (1,)

answers = (
    0,
    0,
)


def test_parts() -> None:
    # Oracle says so
    assert part_1() == 0
    assert part_2() == 0


def verify_day(data: Any, expected_1: Any, expected_2: Any) -> None:
    assert part_1(data) == expected_1
    assert part_2(data) == expected_2


def test_samples() -> None:
    """
    Tests the given examples
    """
    examples = ((sample_seed_1, answers),)

    for (data, expected) in examples:
        verify_day(data, *expected)
