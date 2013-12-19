# Which starting number, under one million, produces the longest Collatz chain?

def Collatz(n):

    chain = [n]

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        chain.append(n)

    return chain

def longest_chain():
    number = 0
    chain_len = 0
    for i in range(1000001, 0, -1):
        chain = Collatz(i)
        if len(chain) > chain_len:
            chain_len = len(chain)
            number = i

    return number, chain_len

if __name__ == "__main__":
    print longest_chain()