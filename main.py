#!/usr/bin/env python3
"""Experiments"""

import subprocess
import sys
from quasigroup import Quasigroup
from db import dataAccess
from time import time as time_time
# from

GENERATORS = ["gen_tri_1", "gen_tri_2", "gen_ort"]


def one_test(generator: int, q_size: int):
    """Execute one test with generating quasigroup and checking it"""
    subprocess.run(["./" + GENERATORS[generator], str(q_size),  "a.output"])
    Q = Quasigroup(file="a.output", from_1=False)
    Q.random_alteration()

    start_time = time_time()
    simple = Q.create_simple()
    ex_time = time_time() - start_time

    simple.export("in.txt")
    result = subprocess.run(["subquasi/prog/r"], capture_output=True,
                            text=True).stdout.rpartition("\n")[0].rpartition("\n")[-1]

    if result != "Easy: No subgroups":
        return False

    subprocess.run(["aff/prog/r"])

    with open("r.txt", "r") as f_res:
        all_lines = f_res.readlines()
        not_aff = True if all_lines[4].find("not affin") >= 0 else False
        one_simple = True if all_lines[8].find("simple") >= 0 else False

    return [GENERATORS[generator], ex_time, 2**q_size, not_aff, one_simple]

if __name__ == "__main__":
    DB = dataAccess()
    counters = [0, 0, 0, 0]  # 3-simple, not aff, 1-simple, all
    for gen in range(3):
        print("Start", gen, ":", end=" ")
        for size in range(3, 12):
            print(size, end="")
            for _ in range(10):
                counters[3] += 1
                print(".", end="")
                res = one_test(gen, size)
                if res:
                    counters[0] += 1
                    counters[1] += 1 if res[3] else 0
                    counters[2] += 1 if res[4] else 0
                    DB.add_exp(*res)
                else:
                    print("AAAAAAAAAAAAAAAAAAAAAAA")
        print()

    print(f"All: {counters[3]}")
    print("3-simple: {0}\nNot affine: {1}\n1-simple: {2}".format(*counters))


    
