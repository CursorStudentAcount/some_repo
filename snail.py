import argparse
import sys
from dataclasses import dataclass
from itertools import cycle
from typing import Tuple, List


def parse_matrix_size(size: str) -> Tuple[int, int]:
    def exit_from_script():
        print("Please enter correct size for matrix")
        sys.exit(0)

    col_numbers, row_numbers = size.split('x')
    try:
        if int(col_numbers) <= 1 or int(row_numbers) <= 1:
            # If it is not a matrix
            exit_from_script()
    except TypeError:
        # if data type is incorrect
        exit_from_script()
    return int(col_numbers), int(row_numbers)


@dataclass
class Position:
    x: int
    y: int


class WayIsFinished(Exception):
    pass


class Snail:

    def __init__(self, column_number, row_number):
        self.left_boarder = 0
        self.right_border = column_number - 1
        self.down_boarder = 0
        self.up_boarder = row_number - 1

        self.directions = cycle([self.move_up, self.move_right, self.move_down, self.move_left])
        self.current_pos = Position(0, 0)

        self.way: List[Position] = [Position(0, 0)]
        self.make_way()

    def move_right(self):
        self.current_pos.x += 1
        if self.current_pos.x > self.right_border:
            raise WayIsFinished()

        self.way.extend([Position(step_x, self.current_pos.y)
                         for step_x in self.get_coordinates(self.current_pos.x, self.right_border)])

        self.up_boarder -= 1
        self.current_pos.x = self.right_border

    def move_left(self):
        self.current_pos.x -= 1
        if self.current_pos.x < self.left_boarder:
            raise WayIsFinished()

        self.way.extend([Position(step_x, self.current_pos.y)
                         for step_x in self.get_coordinates(self.current_pos.x, self.left_boarder, reverse=True)])

        self.down_boarder += 1

        self.current_pos.x = self.left_boarder

    def move_up(self):
        self.current_pos.y += 1
        if self.current_pos.y > self.up_boarder:
            raise WayIsFinished()
        self.way.extend([Position(self.current_pos.x, step_y)
                         for step_y in self.get_coordinates(self.current_pos.y, self.up_boarder)])

        self.left_boarder += 1
        self.current_pos.y = self.up_boarder

    def move_down(self):
        self.current_pos.y -= 1
        if self.current_pos.y < self.down_boarder:
            raise WayIsFinished()

        self.way.extend([Position(self.current_pos.x, step_y)
                         for step_y in self.get_coordinates(self.current_pos.y, self.down_boarder, reverse=True)])
        self.right_border -= 1
        self.current_pos.y = self.down_boarder

    def make_way(self):
        try:
            for move in self.directions:
                move()
        except WayIsFinished:
            pass

    def get_way(self) -> List[Tuple[int, int]]:
        return [(pos.x, pos.y) for pos in self.way]

    @staticmethod
    def get_coordinates(start, end, reverse=False):
        result = list(range(min(start, end), max(start, end) + 1))
        if reverse:
            result.reverse()
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('matrix_size', type=str, help='Input range for matrix. Example: 3x3')

    args = parser.parse_args()
    col_num, size_number = parse_matrix_size(args.matrix_size)

    snail = Snail(col_num, size_number)
    print(snail.get_way())
