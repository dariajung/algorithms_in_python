# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from problem_3 import is_prime

def two_million_primes():
    total = 2
    upper = 2000001
    num = 3
    while num < upper:
        if is_prime(num):
            total += num
            print total
        num += 2
    return total

if __name__ == "__main__":
    print two_million_primes()

