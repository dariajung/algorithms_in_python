# A Pythagorean triplet is a set of three natural numbers, such that
# a < b < c

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# find the product abc

from problem_5 import euclid

def pythagorean():
    a = 0
    b = 0
    c = 0

    for c in xrange(5, 1001):
        for b in xrange(4, c):
            for a in xrange(3, b):
                if a**2 + b**2 == c**2:
                    print a, b, c, a+b+c
                    if a + b + c == 1000:
                        return a*b*c


if __name__ == "__main__":
    print pythagorean()