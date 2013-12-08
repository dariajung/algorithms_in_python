# 2520 is the smallest number that can be divided 
# by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that 
# is evenly divisible by all of the numbers from 1 to 20?

# calculate GCD
def euclid(a, b):
    while a != b:
        if a > b:
            a = a -b
        else:
            b = b - a
    return a

def smallest_multiple(div):
    divisors = list(range(3, div + 1))
    lcd = (1 * 2) / euclid(1, 2)
    for number in divisors:
        lcd = (lcd * number) / (euclid(lcd, number))
    return lcd

if __name__ == "__main__":
   print smallest_multiple(20)