#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    string_arr = s.split(" ")
    outarr = []
    for each in string_arr:
        each = each.capitalize()
        outarr.append(each)
    string = " ".join(outarr)
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
