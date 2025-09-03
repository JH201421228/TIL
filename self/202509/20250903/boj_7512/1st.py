import sys
from collections import defaultdict
from array import array

sys.stdin = open('input.txt')
input = sys.stdin.readline

def sieve_arrays(N: int):
    is_prime = bytearray(b'\x01') * (N + 1)
    is_prime[0] = is_prime[1] = 0

    limit = int(N ** 0.5) + 1
    for i in range(2, limit):
        if is_prime[i]:
            start = i * i
            is_prime[start:N+1:i] = b'\x00' * ((N - start) // i + 1)

    primes = array('I', (i for i in range(N + 1) if is_prime[i]))

    ps = array('Q', [0])
    acc = 0
    for p in primes:
        acc += p
        ps.append(acc)

    return is_prime, primes, ps

def solve(primes: array, ps: array, is_prime_mask: bytearray):
    m = int(input().strip())
    lens = list(map(int, input().split()))
    res = defaultdict(int)

    P = len(primes)

    for nn in lens:
        if nn <= 0 or nn > P:
            continue

        s = ps[nn] - ps[0]
        start = 0
        end = P - nn

        while True:
            res[s] += 1
            if start == end:
                break
            s += primes[start + nn] - primes[start]
            start += 1

    sorted(res)
    for k, v in res.items():
        if v == m and (k <= len(is_prime_mask) - 1 and is_prime_mask[k]):
            print(k)
            return

def main():
    N = 10_000_000
    is_prime_mask, primes, ps = sieve_arrays(N)

    t = int(input().strip())
    for i in range(t):
        print(f"Scenario {i+1}:")
        solve(primes, ps, is_prime_mask)
        print()

if __name__ == "__main__":
    main()
