"""Class for quasigroups."""

import numpy as np
from copy import deepcopy
from random import randint

from numpy.core.numeric import flatnonzero


class Quasigroup(object):
    def __init__(self, size: int = -1, file: str = None, from_1: bool = True,  mark: str = "Q"):
        self.size = size
        self.mark: str = mark  # 1 letter!
        self.loop: bool = False  # full loop, left and right
        self.half_loop: int = 0  # -1 left, 1 right, 0 full or none loop

        if file is None:
            self.data = np.array([[(i + j) % size for i in range(size)]
                                  for j in range(size)], int)
        else:
            if not self.read_from_file(file, from_1):
                raise NameError("Wrong quasigroup in the file!")

    def __str__(self) -> str:
        def one_el(x): return " {:2d}".format(x)
        def one_line(x): return " ".join(map(one_el, x))

        loop_m = ""
        if self.loop:
            loop_m = "F"
        else:
            if self.half_loop > 0:
                loop_m = "R"
            elif self.half_loop < 0:
                loop_m = "L"

        res = "{:2s}│".format(self.mark + loop_m) + one_line(range(self.size))
        res += "\n──│" + "─" * 4 * self.size
        res += "\n 0│"
        res += ("\n{:2d}│".join(map(one_line, self.data)))
        res = res.format(*range(1, self.size))

        return res

    def __bool__(self):
        return self.size != -1

    def __getitem__(self, i: int, j=None):
        """Getter.

        Syntax: self[y] -> np.array or self[y, x] -> int
        """
        if j is None:
            return self.data[i]
        return self.data[i][j]

    def check_correctness(self) -> bool:
        """A simple check for correctness"""
        bit_array: int = 0
        full_line: int = (1 << self.size) - 1
        for line in self.data:
            bit_array = 0
            for el in line:
                if el >= self.size:
                    raise NameError("Incorrect quasigroup operation!")
                mask = (1 << el)
                bit_array |= mask
            if bit_array != full_line:
                raise NameError("Not a quasigroup! " +
                                bin(bit_array) + " " + bin(full_line))
        return True

    def read_from_file(self, file: str, from_1: bool = True) -> bool:
        data = []
        with open(file, "r") as f:
            prev: int = -1
            for row in f.readlines():
                corr: int = 1 if from_1 else 0
                data.append(list(map(lambda x: int(x) - corr, row.split())))

                if prev != -1 and prev != len(data[-1]):
                    return False
                prev = len(data[-1])

        self.size = prev
        self.data = np.array(data, int)

        if not self.check_correctness():
            return False
        return True

    def export(self, file_name: str = "quasigroup.txt"):
        """Export quasigroup to the file"""
        with open(file_name, "w") as f_out:
            for line in self.data:
                print(" ".join(map(lambda x: str(x), line)), file=f_out)

    def transpose_columns(self, i: int, j: int):
        """Transpose two columns"""
        for line in self.data:
            line[i], line[j] = line[j], line[i]

    def transpose_rows(self, i: int, j: int):
        """Transpose rows"""
        self.data[[i, j]] = self.data[[j, i]]

    def _do_loop(self, j: int = 0):
        """Make loop by sorting second column and row (j unit)"""
        self.data = self.data[self.data[:, j].argsort()]
        self.data = self.data[:, self.data[j].argsort()]

        self.loop = True
        return True

    def _do_left_loop(self) -> bool:
        """Make left but not right loop Q(*) from loop (j = 0)"""
        if not self.loop:
            return False

        self.transpose_rows(0, 1)
        self.loop = False
        self.half_loop = -1

        return True

    def _isotope(self) -> bool:
        """Make isotope 2-simple quasigroup from loop"""
        if not self.loop:
            return False

        tmp = deepcopy(self.data[1])
        self.data[1:-1] = self.data[2:]
        self.data[-1] = tmp

        self.loop = False
        self.half_loop = -1

        return True

    def create_simple(self) -> bool:
        """Return 2-simple quasigroup"""
        B = deepcopy(self)
        if not B._do_loop():
            return False
        print()
        print(B)
        print()
        if not B._isotope():
            return False

        B.mark = "S"  # As simple

        return B


if __name__ == "__main__":
    # qua = Quasigroup(10)
    # for _ in range(5):
    #     i, j = randint(0, 9), randint(0, 9)
    #     qua.transpose_rows(i, j)

    #     i, j = randint(0, 9), randint(0, 9)
    #     qua.transpose_columns(i, j)
    qua = Quasigroup(file="ex_2.txt", from_1=False)
    print(qua)
    n = qua.create_simple()
    n.export()
    if not n:
        print("Something went wrong, sorry!")
    else:
        print(n)
