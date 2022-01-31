import unittest

import random

from src.matrix import Matrix
from src.core import compute_pairs


class MatrixTest(unittest.TestCase):
    def test_N_computations(self):
        # This one tests if all pairs are found. So 7x7 matrix sizes should have
        # all 7 pairs.

        size = random.randint(3, 7)

        S1 = [
            random.sample([el for el in range(1, size + 1)], size) for _ in range(size)
        ]
        S2 = [
            random.sample([el for el in range(1, size + 1)], size) for _ in range(size)
        ]

        M1 = Matrix.flatten_square_matrix(S1)
        M2 = Matrix.flatten_square_matrix(S2)
        M1.increase(increase_step=True)
        M2.increase(increase_value_by=10)

        pairs = compute_pairs(M1, M2)

        self.assertEqual(len(pairs), size)

