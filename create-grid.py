import argparse

import my_lib.my_grid as grid


GRID_FILE_NAME = "./resources/grid.txt"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", required=True, type=int, help="Number of random grid rows")
    parser.add_argument("-c", required=True, type=int, help="Number of random grid columns")
    parser.add_argument("-p", required=True, type=float, help="Probability of an obstacle being in a given cell (i,j)")
    args = parser.parse_args()

    if args.r <= 0 or args.c <= 0:
        raise RuntimeError("n and m must be positive integers")
    if args.p < 0 or args.p > 1:
        raise RuntimeError("p must be a probability value (i.e., in [0;1])")

    print("Random game generated:\n")
    grid.generate_grid(args.r, args.c, args.p, GRID_FILE_NAME, show=True)
    print("Grid has been created!")