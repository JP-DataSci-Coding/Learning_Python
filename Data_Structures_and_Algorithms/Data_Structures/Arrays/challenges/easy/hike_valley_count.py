
# ----- Hike Valley Count: Array Exercise -----

# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly n steps, for every
# step it was noted if it was an uphill, U, or a downhill, D, step. Hikes always start and end at sea level, and
# each step up or down represents a 1 unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending
# with a step down to sea level.

# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending
# with a step up to sea level.

# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Constraints

# 2 <= steps <= 10^6

# path[i] is an element of {UD}

# Example

# Path array = [DDUUUUDD]

# Steps = 8

# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally,
# the hiker returns to sea level and ends the hike.

# Returns

# int: the number of valleys traversed

# ----- Solution -----

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here

    valley_count = 0  # O(1)

    altitude = 0  # O(1)

    for i in range(0, steps - 1):
        path_type = path[i]  # O(n)

        if path_type == 'D':
            if altitude == 0:
                valley_count += 1  # O(n)

            altitude -= 1  # O(n)
        else:
            altitude += 1  # O(n)

    return valley_count  # O(1)

# Time complexity is 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
