
# ----- Letter 'a' Count: Array Exercise -----

# There is a string, s, of lowercase English letters that is repeated infinitely many times. Given an integer, n,
# find and print the number of letter a's in the first  letters of the infinite string.

# Example

# s = 'abcac'
# n = 10

# The substring we consider is 'abcacabcac', the first 10 characters of the infinite string. There are 4 occurrences
# of a in the substring.

# Return

# int: the frequency of a in the substring

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    a_count_in_s = s.count('a')

    string_repeats = n // len(s)

    remainder = n % len(s)
    remaining_string = s[0: remainder]

    a_count_in_remain = 0

    if remainder > 0:
        a_count_in_remain = remaining_string.count('a')

    a_full_count = (a_count_in_s * string_repeats) + a_count_in_remain

    return a_full_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
