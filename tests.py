"""Tests by pytest"""

import pytest
from numpy import array_equal
from quasigroup import Quasigroup
from random import randint


@pytest.fixture()
def from_file():
    """Quasigroup from file"""
    return [Quasigroup(file="ex_1.txt"), Quasigroup(file="ex_2.txt", from_1=False)]


@pytest.fixture()
def z_10():
    """Quasigroup Z_10"""
    return Quasigroup(10)


@pytest.fixture()
def changed_z_10():
    """Changed quasigroup Z_10"""
    z_10 = Quasigroup(10)
    for _ in range(5):
        i, j = randint(0, 9), randint(0, 9)
        z_10.transpose_rows(i, j)

        i, j = randint(0, 9), randint(0, 9)
        z_10.transpose_columns(i, j)

    return z_10


def test_all_from_file(from_file):
    """Test making loop (j=0) and left loop (j=1) for file"""
    for qua in from_file:
        do_loop(qua)
        do_left_loop(qua)


def test_all_z_10(z_10):
    """Test making loop (j=0) and left loop (j=1) for Z_10"""
    do_loop(z_10)
    do_left_loop(z_10)


def test_all_changed_z_10(changed_z_10):
    """Test making loop (j=0) and left loop (j=1) for changed Z_10"""
    do_loop(changed_z_10)
    do_left_loop(changed_z_10)


def do_loop(quasigroup: Quasigroup):
    """Test making loop (with j = 0) from quasigroup"""
    quasigroup._do_loop()

    assert array_equal(quasigroup[0], list(range(quasigroup.size)))
    for i in range(quasigroup.size):
        assert i == quasigroup[i][0]


def do_left_loop(quasigroup: Quasigroup):
    """Test making left loop (with j = 1) from quasigroup"""
    quasigroup._do_loop()
    quasigroup._do_left_loop()

    assert array_equal(quasigroup[1], list(range(quasigroup.size)))

    switch: bool = False
    for i in range(quasigroup.size):
        if i != quasigroup[i][1]:
            switch = True
    assert switch == True
