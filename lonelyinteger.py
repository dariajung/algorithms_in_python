#!/usr/bin/py

# There are N integers in an array A. All but one integer occurs in pairs. Your task is to find out that number that occurs only once.

# Input Format

# The first line of the input contains an integer N indicating N integers in the array A. Next line contains N integers each separated by a single space.

# Constraints

# 1 <= N < 100
# N % 2 = 1 ( N is an odd number )
# 0 <= A[i] <= 100, ∀ i ∈ [1, N]

# Output Format

# Output (S) which is the number that occurs only once.

# Sample Input:
# 3
# 1 1 2

# Sample Output:
# 2

# Head ends here
def lonelyinteger(a):
    answer = 0
    num_map = dict();
    for number in a:
        key = number
        if key in num_map.keys():
            num_map[key] += 1
        else:
            num_map[key] = 1
    answer = min(num_map, key=num_map.get)
    return answer


# Tail starts here
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)