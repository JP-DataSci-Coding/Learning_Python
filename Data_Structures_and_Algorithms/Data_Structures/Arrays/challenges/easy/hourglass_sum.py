# ----- Hourglass Sum: Array Exercise -----

# ----- Test Run -----

def hourglassSum(arr):
    # Write your code here

    # We set the largest hourglass sum to -63, as based on the constraint of an element
    # value being between -9 <= number <= 9, the lowest possible sum would be -9 x 7 = -63.
    # If we did not know the constraint then we could just add an if condition in the loop
    # if i == 0 then largest_hourglass_sum = hourglass_sum
    largest_hourglass_sum = -63

    for i in range(4):
        if i <= (3):
            for j in range(4):
                if j <= (3):
                    hourglass_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
                                     + arr[i+1][j+1] +
                                     arr[i+2][j] + arr[i+2][j+1]
                                     + arr[i+2][j+2])  # O(n^2)

                    if hourglass_sum > largest_hourglass_sum:
                        largest_hourglass_sum = hourglass_sum  # O(n^2)

    return largest_hourglass_sum


two_dimension_array = [[-1, -1, 0, -9, -2, -2],
                       [-2, -1, -6, -8, -2, -5],
                       [-1, -1, -1, -2, -3, -4],
                       [-1, -9, -2, -4, -4, -5],
                       [-7, -3, -3, -2, -9, -9],
                       [-1, -3, -1, -2, -4, -5]]

hourglassSum(two_dimension_array)
