# What is the value of the first triangle number to have over five hundred divisors?

from sieve import sieve

def prime_factorize(n):
    """Return a list of the prime factors for a natural number."""
    if n == 1: 
        return [1]
    primes = sieve(int(n**0.5) + 1)
    prime_factors = {}
 
    for p in primes:
        if p * p > n: 
            break
        while n % p == 0:
            if p in prime_factors.keys():
                prime_factors[p] += 1
            else:
                prime_factors[p] = 1
            n /= p
    if n > 1: 
        if p in prime_factors.keys():
            prime_factors[p] += 1
        else:
            prime_factors[p] = 1

    return prime_factors

def triangle(number):
    index = 2
    triangle_num = 1
    divisors = 0
    prime_factors = {}

    while divisors <= number:
        divisors = 0
        triangle_num += index
        prime_factors = prime_factorize(triangle_num)
        for key in prime_factors:
            divisors += prime_factors[key] + 1
        index += 1
        print prime_factors
        print "triangle number ", triangle_num, "divisors ", divisors

    return triangle_num
    

if __name__ == "__main__":
    print triangle(500)



