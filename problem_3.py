#!/usr/bin/py

# Project Euler 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Ugh, so inefficient

import math

def is_prime(num):
    prime = True
    sq_root = math.ceil(num**(1.0/2))
    number = 2

    if (num == 2):
        return prime

    else:
        while number <= sq_root:
            if num % number == 0:
                prime = False
                break
            number += 1

    return prime

def get_factors(num):
    print num
    i = 2
    largest_prime = None
    test = None

    while i < num:
        if num % i == 0 and i == 2:
            test = num / i
            print "test1: ", test
            if is_prime(test):
                largest_prime = test
                break
        elif num % i == 0 and i % 2 == 1:
            test = num / i
            print "test2: ", test
            if is_prime(num / i):
                largest_prime = test
                break
        i+= 1

    return largest_prime

if __name__ == '__main__':
    a = float(raw_input("Enter number: "))
    print get_factors(a)

