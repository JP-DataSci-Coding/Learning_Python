# ----- Exercise: First Recurring Character -----

# Given an array, the function should return the first recurring character.

# Example: [2, 5, 1, 2, 3, 5, 1, 2, 4]
# Returns: 2

def first_recurring_character(array):
    # Check if list is empty or is not list
    if len(array) < 2 or not isinstance(array, list):
        return 'Input must be a list with at least two elements!'
    elif len(array) >= 2 and len(set(array)) == len(array):
        return 'Input must have duplicate elements!'

    dict = create_dictionary_from_array(array)  # O(n)

    for element in array:
        dict[element] += 1  # O(n)

        if dict[element] == 2:
            return element  # O(n)


def create_dictionary_from_array(array):
    # List comprehension
    return {key: 0 for key in array}  # O(n)


# Python by default remembers the order in which the keys were added to the
# dictionary. Not all languages do this!
array = [2, 5, 1, 2, 3, 5, 1, 2, 4]

print(create_dictionary_from_array(array))

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]

# Should return 2

print(first_recurring_character(array))

array = [2, 5, 1, 3, 5, 5, 1, 2, 4]

# Should return 5

print(first_recurring_character(array))

array = ['a', 'b', 'e', 'a', 'b', 'b']

# Should return 'a'

print(first_recurring_character(array))

# Should return error message
print(first_recurring_character('a'))

# Should return error message
print(first_recurring_character(['a', 'b']))
