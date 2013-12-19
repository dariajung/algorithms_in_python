#!/usr/bin/py

# Python Implementation of Sieve of Eratosthenes

def sieve(a):
    num_map = []
    bool_map = [True]*len(range(2, a + 1))
    primes = []

    # Create a dictionary
    # where all key initially 
    # have value of True 
    for num in range(2, a+1):
        num_map.append(num) 

    for num in num_map:
        #print num_map[num]
        index = num_map.index(num)
        for i in range(index + num, len(num_map), num):
            bool_map[i] = False

    for i in range(len(bool_map)):
        if bool_map[i] == True:
            primes.append(num_map[i])

    return primes

if __name__ == '__main__':
    print sieve(10000)
