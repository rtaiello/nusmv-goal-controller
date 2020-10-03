#!/usr/bin/env python3

# my lib
from src.my_lib.costant import *


class Model:

    def __init__(self, grid_path):
        self.path = grid_path
        self.data = None
        self.generate_from_file()

    def generate_from_file(self, controller=False):

        out = open(MODEL_OUTPUT, 'w')
        f = open(self.path)
        raw = f.read()
        f.close()
        self.data = GridData(raw)
        grid_model = open(GRID_MODEL_DIR)
        self.write_main(out, grid_model.read())
        grid_model.close()
        out.close()

    def write_main(self, fd, model):
        code = "MODULE main\n\n"
        code += "DEFINE\n"
        code += "    MATRIX := " + str(self.data.grid) + ";\n"
        code += "    n := " + str(self.data.n) + ";\n"
        code += "    m := " + str(self.data.m) + ";\n"
        code += "    x_start := " + str(list(self.data.entry)[0]) + ";\n"
        code += "    y_start := " + str(list(self.data.entry)[1]) + ";\n"
        code += "    x_goal := " + str(list(self.data.goal)[0]) + ";\n"
        code += "    y_goal := " + str(list(self.data.goal)[1]) + ";\n\n"
        code += "VAR\n    launch_game : game(MATRIX, n, m, x_start, y_start, x_goal, y_goal);\n\n"
        code += "-- END MODULE main\n\n"
        fd.write(code + model)

    def print_grid(self, controller=False):
        for i in range(self.data.n):
            for j in range(self.data.m):
                if self.data.entry == (i, j) and not controller:
                    print(START_POINT, end='')
                elif self.data.goal == (i, j):
                    print(GOAL_POINT, end='')
                elif self.data.grid[i][j] == 0:
                    print(PASS_POINT, end='')
                elif self.data.grid[i][j] == 1:
                    print(OBS_POINT, end='')
            print('\n', end='')
        print('\n', end='')

    def set_entry(self, new):
        if self.data.grid[new[0]][new[1]] == 1 or new[0] not in range(self.data.n) or new[1] not in range(self.data.m):
            raise Exception("Given entry point is an obstacle, or is out of grid bounds")
        self.data.entry = new

    def regenerate(self):
        if self.data == None:
            raise RunTimeError("generate_from_file() must be called before regenerate()")
        out = open(MODEL_OUTPUT, 'w')
        grid_model = open(GRID_MODEL_DIR)
        self.write_main(out, grid_model.read())
        grid_model.close()
        out.close()


class GridData:

    def __init__(self, raw):
        rows = raw.split('\n')
        self.n = len(rows) - 2
        self.m = len(rows[0])
        grid = []

        for i in range(self.n):
            chars = list(rows[i])
            row = []
            for j in range(self.m):
                if chars[j] == OBS_POINT:
                    row.append(1)
                else:
                    row.append(0)
                    if chars[j] == START_POINT:
                        self.entry = (i, j)
                    elif chars[j] == GOAL_POINT:
                        self.goal = (i, j)
            grid.append(row)
        self.grid = grid
