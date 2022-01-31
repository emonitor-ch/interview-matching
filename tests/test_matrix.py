import unittest

from src.matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_initialization_exceptions(self):

        # Check if Matrix contains valid set of all possible values.
        with self.assertRaises(ValueError) as context:
            # For 2x2, it should be 2,1,1,2 or 1,2,2,1
            Matrix([1, 2, 2, 3])
        self.assertEqual(
            "Matrix contains invalid set of elements.", str(context.exception)
        )

    def test_row_retrieval(self):

        m = Matrix([1, 2, 2, 1])

        self.assertListEqual([1, 2], m.retrieve_row(0))
        self.assertListEqual([2, 1], m.retrieve_row(1))

        m = Matrix(
            [
                2,3,1,
                3,2,1,
                3,1,2,
            ]
        )

        self.assertListEqual([2, 3, 1], m.retrieve_row(0))
        self.assertListEqual([3, 2, 1], m.retrieve_row(1))
        self.assertListEqual([3, 1, 2], m.retrieve_row(2))

    def test_column_retrieval(self):

        m = Matrix(
            [
                2,3,1,4,
                3,2,1,4,
                3,1,2,4,
                2,1,4,3,
            ]
        )

        self.assertListEqual([2, 3, 3, 2], m.retrieve_column(0))
        self.assertListEqual([3, 2, 1, 1], m.retrieve_column(1))
        self.assertListEqual([1, 1, 2, 4], m.retrieve_column(2))
        self.assertListEqual([4, 4, 4, 3], m.retrieve_column(3))

    def test_flatten_square_matrix(self):

        m = Matrix.flatten_square_matrix([[1, 2, 3], [3, 2, 1], [1, 2, 3]])

        self.assertEqual(m.size, 3)


if __name__ == "__main__":
    unittest.main()
