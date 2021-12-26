# ----- Sock Pairs: Array Exercise -----

# There is a large pile of socks that must be paired by color. Given an array of integers representing
# the color of each sock, determine how many pairs of socks with matching colors there are.

# Constraints

# 1 <= n <= 100
# 1 <= ar[i] <= 100 where 0 <= i < n

# Example

# n = 7
# ar = [1, 2, 1, 2, 1, 3, 2]

# There is one pair of color and one of color. There are three odd socks left, one of each color. The number
# of pairs is.

# Returns

# int: the number of pairs

# ----- Solution -----

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here

    pairs = 0  # O(1)

    # List comprehension
    sock_colour_dictionary = {key: 0 for key in ar}  # O(n)

    for i in range(len(ar)):
        sock_colour_dictionary[ar[i]] += 1  # O(n)

    for key, val in sock_colour_dictionary.items():
        pairs += (val // 2)  # O(n)

    return pairs  # O(1)

# Time complexity is O(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
