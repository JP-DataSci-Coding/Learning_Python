# ----- Exercise: Reverse A String -----

# Example: 'Hi my name is Andrei'
# Returns: 'ierdnA si eman ym iH'

def reverse_string(string):
    # First check that input is a string
    if isinstance(string, str) == False or len(string) < 2:
        # O(1)
        print('Please return a string input or a string that is more than two characters!')
        return

    # We can split strings into a list of characters like so:
    # str_array = string.split(' ')  # O(n)
    # However, Python allows us to loop through each character of a string
    # so the above syntax is not needed.

    reverse_str_array = []  # O(1)

    # We traverse the array from the last to first by
    # decrementing
    for i in range(len(string)-1, -1, -1):
        reverse_str_array.append(string[i])  # O(n)

    return ''.join(reverse_str_array)  # O(n)


string = 'Hi my name is Andrei'

reverse_string(0)
reverse_string('H')

reversed_string = reverse_string(string)
print(reversed_string)

# ----- Easier Solution -----

# Python actually has a built-in solution for reversing a list:

# stri[::-1]

# The above code basically says:

# list[<start>:<stop>:<step>]

# What this does is it starts from the end towards the first taking each element.
# So it reverses a. This is applicable for lists/tuples as well.
