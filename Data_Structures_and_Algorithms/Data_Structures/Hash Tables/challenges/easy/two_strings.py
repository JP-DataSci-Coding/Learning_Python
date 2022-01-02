# ----- Two Strings: Dictionary Exercise -----

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# Note! All strings are in lowercase

# ----- Optimal Solution -----


def twoStrings(s1, s2):
    # Write your code here
    substring_dictionary = {}

    for char in s1:
        substring_dictionary[char] = 1

    for char in s2:
        if char in substring_dictionary:
            return 'YES'

    return 'NO'

# ----- Test Run -----


s1 = 'and'

s2 = 'art'

# Returns 'YES
print(twoStrings(s1, s2))
