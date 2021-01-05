"""
Advent of Code - Day 3
"""
from functools import reduce, partial
from operator import mul
from enum import Enum
from multiprocessing import Pool
from itertools import starmap
from typing import List, Iterable, Tuple

from aoc.day_03.seed import p1

cores = 16


def part_1(puzzle_input: str = p1) -> int:
    """
    --- Day 3: Toboggan Trajectory ---

    With the toboggan login problems resolved, you set off toward the airport.
    While travel by toboggan might be easy, it's certainly not safe: there's
    very minimal steering and the area is covered in trees. You'll need to see
    which angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer
    coordinates in a grid. You make a map (your puzzle input) of the open
    squares (.) and trees (#) you can see. For example:

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

    These aren't the only trees, though; due to something you read about once
    involving arboreal genetics and biome stability, the same pattern repeats
    to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    You start on the open square (.) in the top-left corner and need to reach
    the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper
    model that prefers rational numbers); start by counting all the trees you
    would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is
    right 3 and down 1. Then, check the position that is right 3 and down 1
    from there, and so on until you go past the bottom of the map.

    The locations you'd check in the above example are marked here with O where
    there was an open square and X where there was a tree:

    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    In this example, traversing the map using this slope would cause you to
    encounter 7 trees.

    Starting at the top-left corner of your map and following a slope of right
    3 and down 1, how many trees would you encounter?
    """
    return get_moves(parse_map(puzzle_input)).count(Obstacle.TREE)


def part_2(puzzle_input: str = p1) -> int:
    """
    --- Part Two ---

    Time to check the rest of the slopes - you need to minimize the probability
    of a sudden arboreal stop, after all.

    Determine the number of trees you would encounter if, for each of the
    following slopes, you start at the top-left corner and traverse the map all
    the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
    respectively; multiplied together, these produce the answer 336.

    What do you get if you multiply together the number of trees encountered on
    each of the listed slopes?
    """
    patterns = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    return get_routes_multiple(parse_map(puzzle_input), patterns)


class Obstacle(str, Enum):
    TREE = "#"
    OPEN = "."


def nth(data: List[Obstacle], pos: int) -> Obstacle:
    return data[pos % len(data)]


def get_move_obstacle(
    row: int, loc_map: List[Obstacle], right_steps: int = 1
) -> Obstacle:
    return nth(loc_map, row * right_steps)


def parse_map(data: str) -> List[List[Obstacle]]:
    # We need to count, slice and dice this data later and send it out to
    # different processes. Hence using lists instead of generators.
    return [list(map(Obstacle, ln)) for ln in data.splitlines()]


def get_moves(
    loc_map: List[List[Obstacle]], right_steps: int = 3, down_steps: int = 1
) -> List[Obstacle]:
    with Pool(processes=cores) as pool:
        moves = pool.starmap(
            partial(get_move_obstacle, right_steps=right_steps),
            enumerate(loc_map[::down_steps]),
        )
    return moves


def get_routes_multiple(
    loc_map: List[List[Obstacle]], patterns: Iterable[Tuple[int, int]]
) -> int:
    routes = starmap(partial(get_moves, loc_map), patterns)
    routes_count = (r.count(Obstacle.TREE) for r in routes)
    return reduce(mul, routes_count)
