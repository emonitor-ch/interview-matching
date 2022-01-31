#!/usr/bin/env python3
"""
The main entry point. Invoke as `python3 -m src'.
"""
import random
import sys

from src.core import compute_pairs
from src.matrix import Matrix


def main():

    size = input("Please enter size of Square Matrix(for example, 3): ")
    try:
        size = int(size)
    except ValueError:
        print("Invalid argument entered, should be greater than 1")
        exit(1)

    choice = input("Do you want to randomly generate matrix elements? (y/n) ")

    if choice == "y" or choice == "yes":
        # Generate Square matrices with random row elements.
        S1 = [
            random.sample([el for el in range(1, size + 1)], size) for _ in range(size)
        ]
        S2 = [
            random.sample([el for el in range(1, size + 1)], size) for _ in range(size)
        ]
    else:
        # Manually enter elements
        exit("Not implemented to enter manually. Exiting...")

    try:
        M1 = Matrix.flatten_square_matrix(S1)
        M2 = Matrix.flatten_square_matrix(S2)

        print("The applicants matrix is: ")
        M1.pretty_print()
        print("The apartments matrix is: ")
        M2.pretty_print()

        M1.increase(increase_step=True)
        M2.increase(increase_value_by=10)

        pairs = compute_pairs(M1, M2)

        # Print matches by order (applicant-apartment).
        print("Pairs are:")
        for pair in pairs:
            print(pair)
    except KeyboardInterrupt:
        # Suppress CTRL + C traceback
        sys.exit(1)


if __name__ == "__main__":
    main()
