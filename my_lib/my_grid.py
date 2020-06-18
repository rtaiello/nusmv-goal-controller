#!/usr/bin/env python3

import random
import io

from my_lib.costant import *


def generate_grid(n_rows: int, n_cols: int, probability: float, out_file: str, show: bool=False) -> None:
    grid = io.StringIO()
    entry = [random.randint(0, n_rows-1), random.randint(0, n_cols-1)]
    goal = [random.randint(0, n_rows-1), random.randint(0, n_cols-1)]
    while entry == goal:
        goal = [random.randint(0, n_cols-1), random.randint(0, n_cols-1)]

    for i in range(n_rows):
        for j in range(n_cols):
            if entry == [i, j]:
                grid.write(START_POINT)
            elif goal == [i, j]:
                grid.write(GOAL_POINT)
            elif probability >= random.random():
                grid.write(OBS_POINT)
            else:
                grid.write(PASS_POINT)
        grid.write("\n")
    grid.write("\n")

    grid = grid.getvalue()
    if show:
        print(grid)

    f = open(out_file, 'w+')
    f.write(grid)
    f.close()
