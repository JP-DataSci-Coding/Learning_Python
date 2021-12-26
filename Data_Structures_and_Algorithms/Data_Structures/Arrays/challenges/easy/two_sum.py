# ----- Exercise: Two Sum Array -----

# Given an array of integers, return the indices of the
# two numbers that add up to a given target.

# Constraints/Assumptions

# 1. Are the numbers positives or negatives? Positives only

# 2. Will there always be a solution? No

# 3. Can the target itself be an element? No

# 4. Are there duplicate numbers? No

# 5. What do we return if there is no solution? None

# 6. Will there be duplicate solutions? No, only one pair will add up to the target

# 7. What is the output format? List of indices

# Example: [1, 5, 9, 20]
# Target: 21
# Returns [0, 3]

# Approaching The Problem

# 1. After having defined the constraints with the interviewer, start writing out some edge cases, i.e.
# extreme scenarios where there is no solution.

# 2. Figure out a solution without code:

# Start with a best case scenario, like the example above so:

# Input array = [1, 5, 9, 20]
# Target = 21
# Output = [0, 3]

# We do not care about the optimal solution at this stage!
# Immediately, a solution would be to test out every single pair in the array.
# This can be done through what is called a "two pointer technique" where one pointer is at the first number
# and the second pointer keeps looping through the other numbers and sums them with the first one. Once all elements
# have been tested, the first pointer moves to the next one.

# 3. Let us write our brute force solution.
# Note! In the interview, it is best to just write it out in pen first and also check for errors as this shows carefulness.

# 4. Test the brute force solution against the test cases.

# 5. Finally, analyse the time and space complexity of the brute force solution.

# ----- Brute Force Solution -----

def two_sum_array_brute_force(array, target):
    # Edge cases
    if not array or len(array) < 2:
        return None
    elif len(array) == 2:
        if (array[0] + array[1]) == target:
            return [0, 1]
        else:
            return None

    # Two pointer technique
    for i in range(len(array)):
        # O(n) as the loop increases with the number of elements/inputs
        # Space complexity is just O(1) as we are just pointing to single integers to execute our calculation rather
        # taking up memory that linearly increases with the size of the array.
        difference = target - array[i]
        for j in range(i + 1, len(array)):
            if array[j] == difference:
                # O(n^2) as the number of times this operation executes will increase with the number of inputs
                return [i, j]
            else:
                # If we get to the second last element, there is no need to check further
                if i == (len(array) - 2):
                    # O(n) as this operation will only ever execute once no matter the size of the input
                    return None
                else:
                    continue  # O(n^2)

# Time = O(n^2)
# Space = O(1)

# ----- Optimal Solution -----

# Now, we saw that the brute force solution had the optimal space complexity of O(1).
# From this, we can immediately see that there may be a way to reduce the time complexity by
# sacrificing a little bit of space complexity efficiency.


def two_sum_array(array, target):
    # Edge cases
    if not array or len(array) < 2:
        return None
    elif len(array) == 2:
        if (array[0] + array[1]) == target:
            return [0, 1]
        else:
            return None

    # Space complexity is O(n) because for each array element we create a
    # key value
    number_dictionary = create_hash_table(array)

    for i in range(len(array)):
        difference = target - array[i]  # O(n)

        is_key = number_dictionary.get(difference, None)  # O(n)

        if is_key is not None:
            return [i, number_dictionary[difference]]  # O(n)


def create_hash_table(array):
    # enumerate() adds a counter to an iterable and returns the index/counter and element in
    # tuple form like so (index, value)
    return {key: index for index, key in enumerate(array)}  # O(n)

# Time = O(n)
# Space = O(n)

# ----- Test Runs -----


array = [1, 5, 9, 20]

target = 21

# Should return [0, 3]

print(two_sum_array(array, target))

array = [5, 5, 9, 20, 30, 3, 1, 8]

target = 28

# Should return [3, 7] or [7, 3]

print(two_sum_array(array, target))

array = [1, 5, 9]

target = 14

# Should return [1, 2]

print(two_sum_array(array, target))

array = [5, 5, 9]

target = 100

# Should return None

print(two_sum_array(array, target))

array = []

target = 100

# Should return None

print(two_sum_array(array, target))
