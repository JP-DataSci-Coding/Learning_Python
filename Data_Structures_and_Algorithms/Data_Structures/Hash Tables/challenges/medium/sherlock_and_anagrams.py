# ----- Sherlock and Anagrams: Dictionary Exercise -----

# ----- Brute Force Solution -----

def get_all_substrings(string):
    substrings = []

    # Dynamic sliding window technique
    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            substrings.append(string[i:j])

    return substrings


string = 'abba'

# print(get_all_substrings(string))


def is_anagram(string_one, string_two):
    if len(string_one) != len(string_two):
        return False  # Can only be anagram if same number of characters

    string_characters = {}

    for char in string_one:
        if char in string_characters:
            string_characters[char] += 1
        else:
            string_characters[char] = 1

    for char in string_two:
        if char in string_characters:
            string_characters[char] -= 1

            if string_characters[char] == 0:
                del string_characters[char]

        else:
            return False  # Not anagram

    return True  # If both loops complete then anagram


def find_number_of_anagrams(string):

    substrings = get_all_substrings(string)

    anagram_count = 0

    for i in range(len(substrings)):
        j = len(substrings) - 1
        while j > i:
            anagram = is_anagram(substrings[i], substrings[j])

            if anagram:
                anagram_count += 1
                del substrings[j]

            j -= 1

    return anagram_count


# Return 4
print(find_number_of_anagrams(string))
