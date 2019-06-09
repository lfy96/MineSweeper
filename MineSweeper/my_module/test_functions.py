"""Test for my functions.

Note: because these are 'empty' functions (return None), here we j and return None, as expected.
"""
from functions import Board


##
##

test = Board(3, 4, 5)

def test_hitMine():
    assert callable(test.hitMine(0, 0))

def test_isWinner():
    assert callable(test.isWinner(0, 0))

def test_updateBoard():
    assert callable(test.updateBoard(0, 0))


