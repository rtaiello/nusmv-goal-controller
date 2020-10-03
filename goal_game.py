#!/usr/bin/env python3

# os libraries
import subprocess

# my libraries
import my_lib.utils as utils
import platform
import my_lib.my_grid as grid
import my_lib.my_model as model
from my_lib.costant import *

if __name__ == "__main__":

    stop = False
    while not stop:
        try:
            n_rows = int(input("Number of rows (range [1..]) \n"))
            n_columns = int(input("Number of columns (range [1..])\n"))
            probability = float(input("Enter a probability (range [0..1])\n"))
            guard = n_rows < 0 or n_columns < 0 or (0 > probability > 1)
        except ValueError:
            print("That's not an int!")
            continue
        if guard:  # if not a positive int print message and ask for input again
            print("Sorry, invalid input, try again")
            continue
        grid.generate_grid(n_rows, n_columns, probability, GRID_FILE_NAME, show=True)
        my_model = model.Model(GRID_FILE_NAME)
        response = str(subprocess.check_output([NUSMV_EXEC, MODEL_OUTPUT]))
        plan = utils.get_path(response)
        if plan is None:
            print("Generated grid doesn't have a valid path")
        else:
            print(utils.interpret_path(plan))
        exit = int(input("Press 0 to exit, 1 to continue... \n"))
        stop = exit == 0
