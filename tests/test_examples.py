import unittest

from src.core import compute_pairs
from src.matrix import Matrix


class ExamplesTest(unittest.TestCase):
    def test_example_1(self):
        m1 = Matrix(
            [
                4,3,1,2,
                2,1,3,4,
                1,3,4,2,
                4,3,1,2,
            ]
        )

        m2 = Matrix(
            [
                3,2,4,1,
                2,3,1,4,
                3,1,2,4,
                3,2,4,1,
            ]
        )

        m1.increase(increase_step=True)
        m2.increase(increase_value_by=10)

        results = compute_pairs(m1, m2)

        # Note: Different from README.md
        self.assertListEqual(results, [13, 22, 31, 44])

    def test_example_2(self):
        m1 = Matrix(
            [
                3, 4, 2, 1, 6, 7, 5,
                6, 4, 2, 3, 5, 1, 7,
                6, 3, 5, 7, 2, 4, 1,
                1, 6, 3, 2, 4, 7, 5,
                1, 6, 5, 3, 4, 7, 2,
                1, 7, 3, 4, 5, 6, 2,
                5, 6, 2, 4, 3, 7, 1
            ]
        )

        m2 = Matrix(
            [
                4, 5, 3, 7, 2, 6, 1,
                5, 6, 4, 7, 3, 2, 1,
                1, 6, 5, 4, 3, 7, 2,
                3, 5, 6, 7, 2, 4, 1,
                1, 7, 6, 4, 3, 5, 2,
                6, 3, 7, 5, 2, 4, 1,
                1, 7, 4, 2, 6, 5, 3
            ]
        )

        m1.increase(increase_step=True)
        m2.increase(increase_value_by=10)

        results = compute_pairs(m1, m2)

        # Note: Different from README.md
        self.assertListEqual(results, [14, 23, 31, 46, 57, 65, 72])
