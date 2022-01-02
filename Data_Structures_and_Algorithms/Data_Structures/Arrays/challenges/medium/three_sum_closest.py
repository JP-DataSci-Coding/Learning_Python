# ----- Three Sum Closest: Array Exercise -----


# Given an integer array nums of length n and an integer target, find three integers in nums such that
# the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# ----- Constraints -----

# 1. 3 <= nums.length <= 1000
# 2. -1000 <= nums[i] <= 1000
# 3. -104 <= target <= 104

# ----- Techniques -----

# - Two pointer
# - Sorting

# ----- Brute Force Solution -----

import sys


def threeSumClosest(nums, target):
    sorted_nums = sorted(nums)  # O(n)

    # sys is a Python module that
    closest_sum = sys.maxsize

    # Two pointer technique
    # One pointer starts at earliest position
    # Second pointer starts at last possible possition
    for i in range(len(sorted_nums)):
        pointer_one = i + 1
        pointer_two = len(sorted_nums) - 1

        while pointer_one < pointer_two:
            sum = sorted_nums[i] + sorted_nums[pointer_one] + \
                sorted_nums[pointer_two]

            difference_from_target = target - sum

            if abs(difference_from_target) < abs(target - closest_sum):
                closest_sum = sum

            # If sum is greater than the target then decrement
            # the second pointer to get a smaller sum
            if (sum > target):
                pointer_two -= 1
            # Else increment the first pointer
            # to get a larger sum
            else:
                pointer_one += 1

    return closest_sum


nums = [-1, 2, 1, -4]
target = 1
# Output should be 2 (=-1 + 2 + 1)
print(threeSumClosest(nums, target))
