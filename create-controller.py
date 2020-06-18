import argparse

import my_lib.my_model as model
import my_lib.my_controller as cnt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, type=str, help="Path to a file representing a valid game grid")
    args = parser.parse_args()

    M = model.Model(args.f)
    M.generate_from_file()
    print("Grid generated from file:\n")
    M.print_grid()
    C = cnt.Controller(M)
    print("Generated moves_dictionary.py")
