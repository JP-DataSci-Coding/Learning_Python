# ----- Exercise 1: O(n) -----

names = ['dory', 'bruce', 'marlin', 'nemo']


def find_nemo(names):
    for name in names:
        name = name.lower()
        if name == 'nemo':
            print('Found Nemo!')


find_nemo(names)

# The find_nemo function takes an array of names and then for each element, it executes two
# operations:

# 1. lower()
# 2. print()

# We can see that the number of operations increases uniformly with the number of elements, i.e.
# four operations with two elements, six operations with three elements etc.

# So, since the number of operations increases linearly with the number of elements, the time
# complexity of the find_nemo function is O(n).

# ----- Exercise 2: O(1) -----


def constant_name(names):
    for name in names:
        print(names[0])
        print(names[1])

# The constant_name function executes two operations no matter the size of the names array.
# This is what we call constant time or O(1), as the number of operations never changes with
# the size of the input.


constant_name(names)

# ----- Exercise 3: Big-O Calculation -----

# What is the Big-O of the code below?


def funChallenge(input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in input:
        anotherFunction()  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)

    return a  # O(1)

# Answer: 3 + 3n = O(n)
# This is because the worst time complexity is O(n) and the numnber of operations
# increases with the number of elements in the input through the for loop.

# ----- Exercise 4: Big-O Calculation -----

# What is the Big-O of the code below?


def anotherFunChallenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in input:
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in input:
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    who_am_i = "I don't know"  # O(1)

# Answer: 4 + 5n = O(n)

# ----- Exercise 5: O(n^2) or Quadratic Time -----

# The code below will log all possible pairs from the boxes array with the
# exception of pairs of the same number. We also do not want duplicate pairs, in
# other words, [1, 2] will be treated as the same as [2, 1].


boxes = [1, 2, 3, 4, 5]

pairs = []


def log_all_pairs(boxes):
    for i in range(len(boxes)):
        first_box = boxes[i]  # O(n)

        for j in range(len(boxes)):
            if j == i:
                # O(n^2) as the number of loop skips will increase with inputs
                continue
            else:
                # O(n^2) as the number of assignments will increase with inputs
                second_box = boxes[j]

                in_pairs = False  # O(n^2)

                # Having three nested loops is usually very bad practice, but for the purposes of this
                # exercise we will just leave it as it is.
                for pair_element in pairs:
                    if first_box in pair_element and second_box in pair_element:
                        in_pairs = True  # O(n^3)
                        break  # O(n^3)

                if in_pairs == False:
                    pairs.append([first_box, second_box])  # O(n^2)

    print(pairs)


log_all_pairs(boxes)

# Answer: O(n^2)
# This is because we have nested for loops. The first for loop goes through every input,
# and then for each input the second for loop will carry out further operations. So, if there
# is an operation that executes linearly with the input in the second for loop, then the time
# complexity is O(n * n), i.e. O(n^2).
