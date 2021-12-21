# Default and non-default parameters and keyword and non-keyword arguments

# Parameters are the names for the data that is to be passed into the function when called
# We see below that we can give parameters default values for when the function is called
# without specific arguments (the values we pass into a function's parameters)
def multiply(num1=5, num2=3):
    print(num1 * num2)


# We can pass argument values using the actual keywords.
multiply(num1=10, num2=20)

# ----- Functions With An Infinite Number Of Arguments -----


def mean(*args):
    return sum(args)/len(args)


print(mean(1, 2, 3, 4, 5, 6))

# Functions can also be defined to take an infinite number of keyworded arguments


def mean(**kwargs):
    return kwargs


print(mean(a=1, b=2, hey=3, wow=4, e=5, v=6))
