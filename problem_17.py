# If all the numbers from 1 to 1000 (one thousand) inclusive 
# were written out in words, how many letters would be used?

# one - nine has 36 letters
# ten has 3 letters
# thousand has 8 letters
# twenty - ninety has 46 letters

def number_letter_count():
    total = 0

    singles = 36
    teens = len('ten') + len('eleven') + len('twelve') + len('thirteen') + len('fourteen') + len('fifteen') + \
    len('sixteen') + len('seventeen') + len('eighteen') + len('nineteen')

    doubles = 46

    total = singles + teens + doubles + doubles * 9 + singles * 8

    hundred = 7
    _and = 3

    hundreds = hundred * 9 + singles
    hundreds += 99 * 9 * (_and + hundred)
    hundreds += 99 * singles
    hundreds += total * 9

    total += hundreds + 11

    return total

if __name__ == "__main__":
    print number_letter_count()
