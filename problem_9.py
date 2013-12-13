# A Pythagorean triplet is a set of three natural numbers, such that
# a < b < c

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# find the product abc

def pythagorean():

    for c in range(5, 1001):
        for b in range(4, c):
            for a in range(3, b):
                if a**2 + b**2 == c**2:
                    print a, b, c, a+b+c
                    if a + b + c == 1000:
                        return a*b*c


if __name__ == "__main__":
    print pythagorean()