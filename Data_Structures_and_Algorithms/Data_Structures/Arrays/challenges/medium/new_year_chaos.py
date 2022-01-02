

# ----- Optimal Solution -----

def minimumBribes(q):
    # Write your code here
    bribes = 0

    # People can only bribe and change their position in the queue, at most, by two places.
    # So, we only need to look at three positions each time, and check if they are the number
    # we expect.
    # We start with the first three positions, we expect them to be in order, i.e. 1, 2 and 3.
    # Then, we loop through each position in the q array, and see if the orders align.
    expectedFirst = 1
    expectedSecond = 2
    expectedThird = 3

    for i in range(len(q)):
        # If q[i] is say 1, then it equals the expectedFirst, so we can look through
        # the next three
        if q[i] == expectedFirst:
            expectedFirst = expectedSecond
            expectedSecond = expectedThird
            expectedThird += 1
        # If q[i] is 2 instead of 1, then we might have 2, 1, 3 or it could be 2, 3, 1 we do not know.
        # But we do know that the second in the queue has bribed the first. Then, because we know the second
        # position is not in its expected place, we can get rid of it and set the expectedSecond as the expectedThird
        # and increment the expectedThird to get 1, 3, 4 because that is the next order that we would expect.
        elif q[i] == expectedSecond:
            bribes += 1
            expectedSecond = expectedThird
            expectedThird += 1
        # Same logic as above.
        elif q[i] == expectedThird:
            bribes += 2
            expectedThird += 1
        # If none of them match so say we have something like 4, 1, 2, this means that the fourth in line
        # has bribed three people to get ahead which breaks the rules so we return 'Too chaotic'.
        else:
            print('Too chaotic')
            return

    print(bribes)
    return
