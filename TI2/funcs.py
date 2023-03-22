import os
from time import perf_counter


def enchipher(filename, target, state):
    # os.system("g++ main.cpp")
    register = int(state, 2)
    # t0 = perf_counter()
    os.system("./a.out {} {} {}".format(register, filename.replace(" ", "\ "), target.replace(" ", "\ ")))
    # t1 = perf_counter()
    # print(t1 - t0)


def bitrepr(val):
    return "".join(str((val >> i) & 1) for i in range(7, -1, -1))
