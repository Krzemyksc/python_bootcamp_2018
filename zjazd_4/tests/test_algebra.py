from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    X = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    Y = [
        [7, 8, 9, ],
        [10, 11, 12],
    ]

    result = add_matrices(X, Y)
    assert result == [
        [8, 10, 12],
        [14, 16, 18],
    ]

def test_sub_matrices():
    X = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    Y = [
        [7, 8, 9, ],
        [10, 11, 12],
    ]

    result = sub_matrices(X, Y)
    assert result == [
        [-6, -6, -6],
        [-6, -6, -6],
    ]
