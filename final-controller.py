import argparse

import my_lib.my_model as mg
import my_lib.utils as cnt

from moves_dictionary import MOVES

def get_best_path(M):
    goal = M.data.goal
    cell = M.data.entry
    result = [cell]
    if not (cell in MOVES) : # Check if there's a path starting from entry
        return None
    while (cell != goal):
        next = MOVES[cell]
        result.append(next)
        cell = next
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, type=str, help="Path to a file representing a valid game grid")
    args = parser.parse_args()

    M = mg.Model(args.f)
    M.generate_from_file()
    print("Grid generated from file:\n")
    M.print_grid()
    path = get_best_path(M)
    if path is not None:
        print(cnt.interpret_path(path))
    else:
        print("Grid generated has not path starting from S leading to G")
