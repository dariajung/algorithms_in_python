#!/usr/bin/py

# Given N integers [N<=10^5], count the total pairs of integers that have a difference of K. [K>0 and K< 1e9]. Each of the N integers will be greater than 0 and at least K away from 2^31-1 (Everything can be done with 32 bit integers).

# Input Format

# 1st line contains N & K (integers).
# 2nd line contains N numbers of the set. All the N numbers are assured to be distinct.

# Output Format

# One integer saying the number of pairs of numbers that have a diff K.

# Sample Input:
# 5 2  
# 1 5 3 4 2 

# Sample Output:
# 3

# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    pairs = {}
    count = 0
    for num in a:
        pairs[num] = 0

    for num in a:
        look_for = abs(num) - abs(k)
        if (pairs.has_key(look_for)):
            count += 1

    answer = count
    return answer

# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)