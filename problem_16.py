# What is the sum of the digits of the number 2^1000?

def power_digit_sum(base, exponent):
    num = base**exponent

    num = str(num)

    _sum = 0

    for digit in num:
        _sum += int(digit)

    return _sum

if __name__ == "__main__":
    print power_digit_sum(2, 1000)