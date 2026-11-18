#!/usr/bin/env python3
"""Exact finite examples accompanying the finite-index amalgam paper."""
from fractions import Fraction
from itertools import product


def rank(matrix):
    rows = [list(map(Fraction, row)) for row in matrix]
    if not rows:
        return 0
    n = len(rows[0])
    pivot_row = 0
    for column in range(n):
        pivot = next((i for i in range(pivot_row, len(rows))
                      if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        leading = rows[pivot_row][column]
        for i in range(pivot_row + 1, len(rows)):
            if rows[i][column]:
                factor = rows[i][column] / leading
                rows[i] = [x - factor * y for x, y in
                           zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def multiply(a, b):
    columns = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, column)) for column in columns]
            for row in a]


def check_rational_cut():
    # Along the second coordinate axis, project onto the line (1, -1).
    x = [[1, 1]]
    y = [[1], [-1]]
    e = [[1, 0], [-1, 0]]
    one_minus_e = [[0, 0], [1, 1]]
    assert multiply(e, e) == e
    assert rank(multiply(x, y)) == 0
    assert rank(multiply(x, e)) + rank(multiply(one_minus_e, y)) == 0
    assert rank(x) == rank(y) == 1


def check_dihedral():
    # An element (j, sign) sends k to (-1)^sign k + j mod n.
    for n in range(2, 21):
        elements = list(product(range(n), range(2)))
        ix = {g: i for i, g in enumerate(elements)}
        s = (0, 1)
        t = (-1, 1)

        def compose(a, b):
            return ((a[0] + (-1 if a[1] else 1) * b[0]) % n,
                    (a[1] + b[1]) % 2)

        def twice_projection(a):
            matrix = [[0] * len(elements) for _ in elements]
            for j, g in enumerate(elements):
                matrix[j][j] += 1
                matrix[ix[compose(a, g)]][j] += 1
            return matrix

        x = twice_projection(s)
        y = twice_projection(t)
        assert rank(x) == rank(y) == n
        # In a finite quotient, one character is lost precisely for even n.
        expected_product_rank = n - (1 if n % 2 == 0 else 0)
        assert rank(multiply(x, y)) == expected_product_rank


def check_thresholds():
    # All subspaces of F_2^2, encoded by their sets of vectors.
    zero = frozenset([0])
    lines = [frozenset([0, v]) for v in (1, 2, 3)]
    whole = frozenset(range(4))
    spaces = [zero, *lines, whole]
    weights = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]

    def dimension(space):
        return len(space).bit_length() - 1

    for targets in product(spaces, repeat=3):
        overlap = {v: sum(w * dimension(v & s)
                          for w, s in zip(weights, targets))
                   for v in spaces}
        boundary = {Fraction(0), Fraction(1)}
        for v, u in product(spaces, repeat=2):
            difference = dimension(v) - dimension(u)
            if difference:
                t = (overlap[v] - overlap[u]) / difference
                if 0 < t < 1:
                    boundary.add(t)

        def greatest(t):
            scores = {v: overlap[v] - t * dimension(v) for v in spaces}
            maximum = max(scores.values())
            maximizers = [v for v in spaces if scores[v] == maximum]
            greatest_spaces = [v for v in maximizers
                               if all(u <= v for u in maximizers)]
            assert len(greatest_spaces) == 1
            return greatest_spaces[0]

        ordered = sorted(boundary)
        for t in ordered:
            greatest(t)
        integral = sum((b - a) * dimension(greatest((a + b) / 2))
                       for a, b in zip(ordered, ordered[1:]))
        assert integral == sum(w * dimension(s) for w, s in zip(weights, targets))


def check_level_and_indices():
    identity = [[1, 0], [0, 1]]
    g = [[0, -1], [1, 10]]

    def power_mod(a, exponent, modulus):
        answer = identity
        for _ in range(exponent):
            answer = [[v % modulus for v in row] for row in multiply(answer, a)]
        return answer

    def order_mod(a, modulus):
        return next(n for n in range(1, 9)
                    if power_mod(a, n, modulus) == identity)

    assert [order_mod(g, q) for q in (5, 7)] == [4, 8]
    for n in range(1, 8):
        assert order_mod(power_mod(g, n, 5), 5) != order_mod(power_mod(g, n, 7), 7)
    assert 1 + 12 * (7 - 1) == 73
    assert 1 + 8 * (11 - 1) == 81


if __name__ == "__main__":
    check_rational_cut()
    print("Rational cut: the non-coordinate minimizing line has cost zero.")
    check_dihedral()
    print("Dihedral quotients: exact regular-representation ranks for orders 4 to 40.")
    check_thresholds()
    print("Threshold model: greatest maximizers and exact integrals for all 125 triples.")
    check_level_and_indices()
    print("Arithmetic: reduction orders 4 and 8, seven nontrivial powers, both Schreier indices.")

