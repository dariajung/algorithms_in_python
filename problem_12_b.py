def triangle(n):
    index = 2
    triangle_num = 1
    divisors = 0

    while divisors <= n + 1:
        divisors = 0
        triangle_num += index

        for num in range(2, triangle_num + 1):
            print num
            if n % num == 0:
                divisors += 1
        index += 1
        print divisors

    return triangle_num


if __name__ == "__main__":
    print triangle(500)