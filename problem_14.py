# Which starting number, under one million, produces the longest Collatz chain?

memoized = {}

def Collatz(n):
    global memoized
    if n in memoized:
        return memoized[n]
    else:
        start = n
        chain = 1
        while n != 1:
            if n in memoized:
                memoized[start] = memoized[n] + chain
                return memoized[n] + chain
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            chain += 1
        memoized[start] = chain
        return chain

def longest_chain():
    number = 0
    chain_len = 0
    for i in range(1, 1000001):
        chain = Collatz(i)
        if chain > chain_len:
            chain_len = chain
            number = i

    return number, chain_len

if __name__ == "__main__":
    print longest_chain()