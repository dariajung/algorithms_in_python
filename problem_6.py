# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 

# 3025 - 385 = 2640

# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum.

def sum_square_diff(number):
    square_of_sum = ((number * (number + 1)) / 2)**2
    sum_of_squares = 0
    i = 1
    while i <= number:
        sum_of_squares += i**2
        i += 1
    diff = abs(square_of_sum - sum_of_squares)
    return diff


if __name__ == "__main__":
    print sum_square_diff(100)