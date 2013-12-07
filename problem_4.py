# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
    reverse = number[::-1]
    if reverse == number:
        return True
    else:
        return False

# first brute force approach
# nested for loop, loop through all possibilities
# 999 - 100 is the range of 3 digit numbers

def largest_palindrome():
    largest = 0
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            number = i * j
            if is_palindrome(str(number)):
                if number > largest:
                    largest = number
    return largest

if __name__ == '__main__':
    print largest_palindrome()