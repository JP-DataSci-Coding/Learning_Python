#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    clouds = len(c)  # O(1)

    finished_game = False  # O(1)

    jumps = 0  # O(1)
    i = 0  # O(1)

    while not finished_game:
        if i < (clouds - 1):
            if i < (clouds - 2) and c[i + 2] != 1:
                jumps += 1  # O(n)
                i += 2  # O(n)
            elif c[i + 1] != 1:
                jumps += 1  # O(n)
                i += 1  # O(n)
        else:
            finished_game = True  # O(n)

    return jumps  # O(1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
