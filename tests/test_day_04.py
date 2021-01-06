from typing import Any

from aoc.day_04.core import part_1, part_2

sample_seed_1 = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip()

answers = (
    2,
    2,
)


def test_parts() -> None:
    # Oracle says so
    assert part_1() > 238
    assert part_1() == 256
    # Less should be valid for part two
    assert part_2() < 256
    assert part_2() > 193
    assert part_2() < 209
    assert part_2() < 207
    assert part_2() == 198


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
