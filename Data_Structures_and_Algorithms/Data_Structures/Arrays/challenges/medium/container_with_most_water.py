# ----- Container With Most Water: Array Exercise -----

# You are given an integer array where each element represents the height, with a length of n. There are n vertical
# lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Area is calculated by h x w

# ----- Constraints -----

# 1. Do the thickness of the lines affect the area? No

# 2. Do the left and right sides of the graph count as walls? No

# 3. Do lines in the middle affect the area? No

# 4. Does each line in the x-axis count as one unit? Yes

# ----- Techniques -----

# - Two pointer
# - Greedy

# ----- Brute Force Solution -----

def container_with_most_water(height):
    # Space is O(1) because we just assigning an integer
    largest_area = 0  # O(1)

    for i in range(len(height)):
        # Space is just O(1) as we are just assigning an integer
        area = 0  # O(n)
        for j in range(i+1, len(height)):
            if height[i] > height[j]:
                # Space is just O(1) as we are just assigning an integer
                area = height[j] * (j - i)  # O(n^2)
            else:
                # Space is just O(1) as we are just assigning an integer
                area = height[i] * (j - i)  # O(n^2)

            if area > largest_area:
                # Space is just O(1) as we are just assigning an integer
                largest_area = area  # O(n^2)

    return largest_area  # O(!)

# Again before we move onto the optimal solution let us first analyse the
# time and space complexity

# Time = O(n^2)
# Space = O(1)
# Space is just O(1) because the actual SIZE of storage or memory does not actually change with
# input size, all we ever do is just assign an integer.

# ----- Optimal Solution -----


def create_dictionary(array):
    return {key: index for index, key in enumerate(array)}


def container_with_most_water(height):
    largest_area = 0

    area = 0

    i = 0
    j = len(height) - 1

    # We do not need to look at the last height because
    # we would have already looped by every possible area by then.
    while i < len(height) - 1:
        first_height = height[i]

        if first_height <= height[j]:
            area = first_height * (j - i)
            i += 1
        else:
            if height[j] > (largest_area / j):
                area = height[j] * (j - i)

            j -= 1

        if area > largest_area:
            largest_area = area

    return largest_area


height = [2, 3, 4, 5, 18, 17, 6]

print(container_with_most_water(height))
