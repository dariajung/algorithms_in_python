# Which starting number, under one million, produces the longest Collatz chain?

class Collatz:
    def __init__(self):
        self.memoized = {}

    def calculate_chain(self, n):
        if n in self.memoized:
            return self.memoized[n]
        else:
            start = n
            chain = 1
            while n != 1:
                if n in self.memoized:
                    self.memoized[start] = self.memoized[n] + chain
                    return self.memoized[n] + chain
                if n % 2 == 0:
                    n /= 2
                else:
                    n = 3*n + 1
                chain += 1
            self.memoized[start] = chain
            return chain

# start to end is the range of 
# number of chains you want to calculate for
def longest_chain(start, end):
    number = 0
    chain_len = 0
    collatz = Collatz()
    for i in range(start, end + 1):
        chain = collatz.calculate_chain(i)
        if chain > chain_len:
            chain_len = chain
            number = i

    return number, chain_len

if __name__ == "__main__":
    print longest_chain(1, 1000001)