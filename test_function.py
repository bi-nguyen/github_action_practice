from function1 import addfunc, subfunc, mulfunc


def test_add():
    assert addfunc(1, 2) == 3
    assert addfunc( 2, 3) == 5
    assert addfunc(3, 4) == 7

def test_sub():
    assert subfunc(1, 2) == -1
    assert subfunc( 2, 3) == -1
    assert subfunc(3, 4) == -1
    assert subfunc(4, 5) == -1

def test_mul():
    assert mulfunc(1, 2) == 2
    assert mulfunc( 2, 3) == 6
    assert mulfunc(3, 4) == 12
