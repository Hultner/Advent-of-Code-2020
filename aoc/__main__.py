from typing import Tuple

from aoc.day_01 import core as day_01

from aoc.day_02 import core as day_02
# from aoc.day_03 import core as day_03
# from aoc.day_04 import core as day_04


def main() -> None:
    puzzles: Tuple = (
        (day_01.part_1(), day_01.part_2()),
        (day_02.part_1(), day_02.part_2()),
        # (day_03.part_1(), day_03.part_2()),
        # (day_04.part_1(), day_04.part_2()),
    )

    for (day, parts) in enumerate(puzzles, start=1):
        print(f"Day {day}:")
        for (part, result) in enumerate(parts, start=1):
            print(f"\tPart {part}: {result}")

    return None


if __name__ == "__main__":
    main()



# from aoc.day_02 import core as d2
# v = """
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """
# d2.PasswordDBValidator(passwords=v)
