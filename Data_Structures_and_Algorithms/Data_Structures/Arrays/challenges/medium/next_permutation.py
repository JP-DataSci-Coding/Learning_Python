# ----- Next Permutation: Array Exercise -----


# ----- Optimal Solution -----

def nextPermutation(nums):
    has_greater_permutation = False

    if len(nums) == 2 or len(nums) == 1:
        start_index = 0
    else:
        start_index = 1

    for i in range(start_index, len(nums)-1):
        if len(nums) == 0:
            has_greater_permutation = True
            break
        elif nums[i] < nums[i+1]:
            first_num = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = first_num
            has_greater_permutation = True
            break

    if not has_greater_permutation:
        j = len(nums) - 1

        original_first_num = nums[0]

        while j > 0:
            if nums[j] > nums[0]:
                nums[0] = nums[j]
                nums[j] = original_first_num

                nums[1:] = sorted(nums[1:])

                break
            else:
                j -= 1

        if j == 0:
            nums.sort()

    return nums


nums = [3, 2, 1]

# Output = [1, 2, 3]

print(nextPermutation(nums))

nums = [1, 2, 3]

# [1, 3, 2]

print(nextPermutation(nums))

nums = [1, 1, 5]

# [1, 5, 1]

print(nextPermutation(nums))

nums = [3, 9, 4, 2, 1]

# [4, 1, 2, 3, 9]

print(nextPermutation(nums))

nums = [5, 4, 7, 5, 3, 2]

# [5, 5, 2, 3, 4, 7]

print(nextPermutation(nums))
