import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi
N = 1_000_000


def fft(v, inv):
    n = len(v)

    j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b:
            j ^= b
            b >>= 1
        j ^= b

        if i < j: v[i], v[j] = v[j], v[i]

    k = 1
    while k < n:
        a = (PI/k) if inv else -(PI/k)
        w = complex(math.cos(a), math.sin(a))

        for i in range(0, n, k<<1):
            wp = 1 + 0j
            for j in range(k):
                x = v[i+j]
                y = v[i+j+k] * wp

                v[i+j] = x + y
                v[i+j+k] = x - y

                wp *= w

        k <<= 1

    if inv:
        for i in range(n):
            v[i] /= n

    return


def fft_wrapper(u, v):
    n = 1
    length = len(u)

    while n < length:
        n <<= 1
    n <<= 1

    u.extend([0j] * (n - length))
    v.extend([0j] * (n - len(v)))

    fft(v, False)
    fft(u, False)

    for i in range(n):
        u[i] *= v[i]

    fft(u, True)

    for i in range(n):
        u[i] = round(u[i].real)

    return u


def sieve(n):
    isPrime = [1] * (n+1)
    isPrime[0] = 0
    isPrime[1] = 0

    for i in range(2, int(n**.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    isPrime[2] = 0
    return isPrime


def solve():
    prime = sieve(N)
    semi = [0] * (N+1)
    for i in range(N+1):
        if prime[i] and 2*i < N+1:
            semi[2*i] = 1
    semi[4] = 1

    res = fft_wrapper(prime, semi)

    return res


def main():
    res = solve()
    for _ in range(int(input())):
        print(res[int(input())])
    return


if __name__ == "__main__":
    main()