"""
Day 2
"""
from typing import Any, Dict, Generator, List

import regex
from pydantic import BaseModel, PositiveInt, Field, constr, validator

from aoc.day_02.seed import p1


def part_1(puzzle_input: str = p1) -> int:
    """
    --- Day 2: Password Philosophy ---

    Your flight departs in a few days from the coastal airport; the easiest way
    down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
    "Something's wrong with our computers; we can't log in!" You ask if you can
    take a look.

    Their password database seems to be a little corrupted: some of the
    passwords wouldn't have been allowed by the Official Toboggan Corporate
    Policy that was in effect when they were chosen.

    To try to debug the problem, they have created a list (your puzzle input)
    of passwords (according to the corrupted database) and the corporate policy
    when that password was set.

    For example, suppose you have the following list:
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each line gives the password policy and then the password. The password
    policy indicates the lowest and highest number of times a given letter must
    appear for the password to be valid. For example, 1-3 a means that the
    password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid. The middle password, cdefg, is
    not; it contains no instances of b, but needs at least 1. The first and
    third passwords are valid: they contain one a or nine c, both within the
    limits of their respective policies.

    How many passwords are valid according to their policies?
    """
    return sum(1 for password in parse(puzzle_input).passwords if password.valid)


def part_2(puzzle_input: str = p1) -> int:
    """
    --- Part Two ---

    While it appears you validated the passwords correctly, they don't seem to
    be what the Official Toboggan Corporate Authentication System is expecting.

    The shopkeeper suddenly realizes that he just accidentally explained the
    password policy rules from his old job at the sled rental place down the
    street! The Official Toboggan Corporate Policy actually works a little
    differently.

    Each policy actually describes two positions in the password, where 1 means
    the first character, 2 means the second character, and so on. (Be careful;
    Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
    of these positions must contain the given letter. Other occurrences of the
    letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:
    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

    How many passwords are valid according to the new interpretation of the
    policies?
    """
    return sum(
        1 for password in parse(puzzle_input).passwords if password.valid_corperate
    )


class PasswordTest(BaseModel):
    min_occurences: PositiveInt
    max_occurences: PositiveInt
    character: str = Field(min_length=1, max_length=1, strip_whitespace=True)
    password: str
    valid: bool = False  # Will be set True if valid
    valid_corperate: bool = False  # Will be set True if valid

    @validator("valid", always=True)
    def check_password(cls, v: Any, values: Dict[str, Any]) -> bool:
        "Validates passwords according to quirky sled company policy"
        try:
            return (
                values.get("min_occurences")
                <= values.get("password", "").count(values.get("character"))
                <= values.get("max_occurences")
            )
        except TypeError:
            return False

    @validator("valid_corperate", always=True)
    def check_password_copreate(cls, v: Any, values: Dict[str, Any]) -> bool:
        "Validates passwords according to strict Toboggan Corporate Policy"
        # Set names in local scope for readability
        idx_1 = values.get("min_occurences", 0) - 1
        idx_2 = values.get("max_occurences", 0) - 1
        char = values.get("character", "")
        password = values.get("password", "")

        return (password[idx_1] == char) ^ (password[idx_2] == char)


class PasswordDBValidator(BaseModel):
    passwords: List[PasswordTest]

    @validator("passwords", pre=True)
    def parse_passwords(cls, v: str) -> Generator[Dict[str, str], None, None]:
        pattern = (
            r"(?P<min_occurences>\d+)-(?P<max_occurences>\d+)"
            r" (?P<character>\w): (?P<password>.*)"
        )
        re = regex.compile(pattern)
        return (re.match(ln).groupdict() for ln in v.strip().splitlines())


def parse(input: str) -> PasswordDBValidator:
    return PasswordDBValidator(passwords=input)
