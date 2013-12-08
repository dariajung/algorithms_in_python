# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from problem_3 import is_prime

def get_prime():
    prime_list = []
    i = 2
    while len(prime_list) <= 10000:
        if is_prime(i):
            prime_list.append(i)
        i += 1
    return prime_list[-1]


if __name__ == "__main__":
    print get_prime()