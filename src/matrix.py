from functools import reduce
from math import sqrt
from operator import add


class Matrix:
    def __init__(self, array: list):
        """Initialize a matrix from a 1D array.

        Array(Matrix) must follow the rules:
        - Be square matrices
        - Each row should have non repeating elements
        - All elements in row should be numbers from 1 to size of matrix.

        Example Matrix:

        ```
        Matrix([
            1,2,
            2,3
        ])
        ```
        """

        self.__size = int(sqrt(len(array)))

        # The sum of all elements in Square Matrix should be matrix size times
        # it's elements from 1 to `size` (inclusive).
        # Example: 3x3 matrix should have 1, 2 and 3 numbers exactly 3 times.
        #          4x4 matrix should have 1,2,3 and 4 numbers exactly 4 times.
        if sum(array) != self.__size * sum([val + 1 for val in range(self.__size)]):
            raise ValueError("Matrix contains invalid set of elements.")

        # Each row should not have repeating elements and all elements should
        # be in range from 1 to `size` of matrix(inclusive).
        for increment in range(self.__size):
            row = array[self.__size * increment : self.__size * (increment + 1) :]
            if len(set(row)) != len(row):
                raise ValueError("The row contains repeating elements")

        self.__array = array.copy()

    def retrieve_row(self, row_number: int):
        """Retrieve a row from matrix based on given `row_number`."""

        return self.__array[self.__size * row_number : self.__size * (row_number + 1) :]

    def retrieve_column(self, column_number: int):
        """Retrieve a column from matrix based on given `column_number`."""

        return self.__array[column_number :: self.__size]

    @classmethod
    def flatten_square_matrix(cls, _matrix: list[list]):
        """Convert 2D array into 1D array.

        This is constructor overload to enable matrix initialization from 2D
        array of elements.

        Example:
        ```
        Matrix.flatten_square_matrix([
            [1,2,3],
            [3,2,1],
            [1,2,3]
        ])
        ```
        """
        return cls(reduce(add, _matrix))

    @property
    def size(self):
        """Returns size of square matrix as integer."""
        return self.__size

    def increase(self, increase_step=False, increase_value_by=1):
        """Increase elements by defined parameters.

        `increase step` will increase all row elements by who they belong to.
        `increase_value_by` will increase all elements of matrix by provided
        value.
        """

        array = self.__array.copy()
        self.__array = list()

        if increase_value_by > 1:
            # Increase all values by multiplier.
            array = [element * increase_value_by for element in array]

            for increment in range(self.__size):
                # Retrieve a row from 1D matrix
                row = array[self.__size * increment : self.__size * (increment + 1) :]
                # For each element inside row, add it's belonging.
                for element in row:
                    value = element + (increment + 1)
                    self.__array.append(value)

        elif increase_step:

            for increment in range(self.__size):
                # Retrieve a row from 1D matrix
                row = array[self.__size * increment : self.__size * (increment + 1) :]
                # For each element inside row, add it's belonging.
                for element in row:
                    value = element + ((increment + 1) * 10)
                    self.__array.append(value)

    def pretty_print(self):
        """Utility method to print all elements of Matrix."""
        for counter in range(self.__size):
            print(self.retrieve_row(counter))
