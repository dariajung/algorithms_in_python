# What is the value of the first triangle number to have over five hundred divisors?
import numbers

class Memoize:
    def __init__(self):
        self.memo = []
        with open('primes.txt') as inputfile:
            for line in inputfile:
                temp = line.strip().split(', ')
                temp = map(int, temp)
                for item in temp:
                    self.memo.append(item)

def prime_factorize(n):
    if n == 1: 
        return [1]
    primes = Memoize()
    prime_factors = {}
 
    for p in primes.memo:
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
    divisors = 1
    prime_factors = {}

    while divisors <= number:
        divisors = 1
        triangle_num += index
        prime_factors = prime_factorize(triangle_num)
        for key in prime_factors:
            divisors *= prime_factors[key] + 1
        index += 1

    return triangle_num
    

if __name__ == "__main__":
    print triangle(500)



