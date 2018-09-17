from nqueens import nqueens


def test_nqueens():
    assert nqueens(0, 4, []) == 2
    assert nqueens(0, 8, []) == 92
