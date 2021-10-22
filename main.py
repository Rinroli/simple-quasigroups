#!/usr/bin/env python3
"""Experiments"""

import subprocess
import sys
from quasigroup import Quasigroup
from db import dataAccess
# from

GENERATORS = ["gen_tri_1", "gen_tri_2", "gen_org"]


def one_test(generator: int, q_size: int):
    """Execute one test with generating quasigroup and checking it"""

    # db_data = []
    # subprocess.run(["echo", "trt"])
    subprocess.run(["./" + GENERATORS[generator], str(q_size),  "a.output"])
    Q = Quasigroup(file="a.output", from_1=False)
    Q.random_alteration()
    simple = Q.create_simple()
    simple.export("in.txt")
    result = subprocess.run(["subquasi/r"], capture_output=True,
                            text=True).stdout.rpartition("\n")[0].rpartition("\n")[-1]
    # db_data.append(GENERATORS[generator])
    # db_data.append(-1)
    if result != "Easy: No subgroups":
        return False
    
    return [GENERATORS[generator], -1, q_size, True, True]


if __name__ == "__main__":
    # db_exp = one_test(1, 4)
    DB = dataAccess()
    res = one_test(1, 4)
    print(res)
    if res:
        DB.add_exp(*res)
    # _, gen, size = sys.argv
    # gen = int(gen)
    # size = int(gen)
    # result = subprocess.run(
    #     ["tri_1", "5"], capture_output=True, text=True
    # )
    # print(result)

    # Q = Quasigroup(file="a.output", from_1=False)
    # Q.random_alteration()

    # print(Q)
    # print()
    # res = Q.create_simple()
    # res.export()
    # print()
    # print("RENAMED")
    # Q.rename_elements()
    # print(Q)
    # print()
    # print(Q.create_simple())
