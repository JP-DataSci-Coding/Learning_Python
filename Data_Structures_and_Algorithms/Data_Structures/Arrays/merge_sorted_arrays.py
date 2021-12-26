# ----- Exercise: Merge Sorted Arrays -----

# Given two arrays, can you sort them and merge them so that
# the resulting array is still in order.

# Assume that the input will always be a list of integers.
# Example: [0, 3, 4, 31] and [4, 6, 30]
# Returns: [0, 3, 4, 4, 30, 31]

# Scenarios:

# [0, 3, 4, 31] and [2, 6, 30, 33] = [0, 3, 4, 4, 6, 30, 31, 33]
# [0, 3, 4, 31] and [4, 4, 6, 30, 33]
# [0, 3, 4, 31] and [2, 4, 4]

def merge_sorted_arrays(arr1, arr2):
    arr1_length = len(arr1)
    arr2_length = len(arr2)

    if arr1_length == 0:
        return arr2.sort()
    elif arr2_length == 0:
        return arr1.sort()

    arr1.sort()  # O(a)
    arr2.sort()  # O(b)

    sorted_array = []

    i = 0
    j = 0

    arr1_element = arr1[i]
    arr2_element = arr2[j]

    # while loops are good for problems where the number of iterations required
    # is unknown. This is in contrast to for loops where the number of iterations
    # or at least the general number of iterations is known.
    while (arr1_element or arr2_element):  # O(a * b)
        # Eventually arr1_element and arr2_element will be undefined or None, so
        # we need to account for that condition
        if arr1_element is not None and arr1_element < arr2_element:
            sorted_array.append(arr1_element)  # O(a)
            i += 1  # O(a)

            if i <= (arr1_length - 1):
                arr1_element = arr1[i]  # O(a)
            else:
                arr1_element = None  # O(a)
        else:
            sorted_array.append(arr2_element)  # O(b)
            j += 1  # O(b)

            if j <= (arr2_length - 1):
                arr2_element = arr2[j]  # O(b)
            else:
                arr2_element = None  # O(b)

    return sorted_array  # O(1)


array1 = [0, 3, 4, 31]
array2 = [4, 4, 6, 30, 33]

# Should return [0, 3, 4, 4, 4, 6, 30, 31, 33]

print(merge_sorted_arrays(array1, array2))

# ----- Easy Solution: Not Interview Appropriate -----


def mergesortedarr(arr1, arr2):
    x = arr1 + arr2
    x.sort()

    return x
