# ----- Exercise 1: O(n) -----

# Say we have a function that creates an array of n elements of the word "hi":
def array_of_n_elements_of_the_word_hi(n):
    hi_array = []  # We declare a list data structure, O(1)

    for i in range(n):  # We declare the i variable, but only once so O(1)
        hi_array.append('Hi')  # We add an element n-times so, O(n)

    return hi_array  # O(1)

# Answer: O(n)
