# ----- Left Rotation: Array Exercise -----

# ----- Test Run -----

def rotLeft(a, d):
    # Write your code here

    rotations = 0

    while rotations < d:
        removed_number = a.pop(0)  # O(a)
        a.append(removed_number)  # O(d)

        rotations += 1  # O(d)

    return a  # O(1)

# Time = O(a) or O(n)
# Space = O(a) or O(n)
