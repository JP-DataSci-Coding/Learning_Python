# 4 x 4 = 16 bytes of memory stored in RAM if machine is a 32-bit system, i.e. 32/8 = 4
# shelf system. Each element takes 4 shelves which is why 4 x 4.
string_array = ['a', 'b', 'c', 'd']

# Push
# Just adds element to the end of the array without looping through anything.
# The compiler does this by just accessing the last element by index/address, so
# O(1).
string_array.append('e')

# Pop
# Just deletes last element of list, again O(1).
string_array.pop()

# Lookup
# Just reads the element by index/address so O(1).
string_array[2]


# Insert
# Say we want to add 'x' to the start of the list. The machine would need to shift
# the other elements by one index, which is why we get O(n).
string_array.insert(0, 'x')

# Now, we add 'y' to the middle of the list. In this case we only need to shift a few
# elements, but this still depends on the size of the input, so we get O(n).
string_array.insert(2, 'y')
