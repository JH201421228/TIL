import math
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi
n = 1_000_000
N = 1 << 20
isPrime = [0] * (N<<1)
oddPrime = [0] * N

def fft(v, inv):
    j = 0
    for i in range(1, N):
        b = N >> 1
        while j & b:
            j ^= b
            b >>= 1
        j ^= b

        if i < j: v[i], v[j] = v[j], v[i]

    k = 1
    while k < N:
        a = (PI/k) if inv else -(PI/k)
        w = complex(math.cos(a), math.sin(a))

        for i in range(0, N, k<<1):
            wp = 1 + 0j
            for j in range(k):
                x = v[i+j]
                y = v[i+j+k] * wp

                v[i+j] = x + y
                v[i+j+k] = x - y

                wp *= w

        k <<= 1

    if inv:
        for i in range(N):
            v[i] /= N

    return


def fft_wrapper(u):
    fft(u, False)

    for i in range(N):
        u[i] *= u[i]

    fft(u, True)

    return


def sieve():
    for idx in range(n):
        isPrime[idx] = 1

    isPrime[0] = 0
    isPrime[1] = 0

    for i in range(2, int(n**.5)+1):
        if isPrime[i]:
            for j in range(i**2, n+1, i):
                isPrime[j] = 0

    for idx in range(N):
        oddPrime[idx] = isPrime[idx*2+1]

    return


def main():
    sieve()

    fft_wrapper(oddPrime)

    for _ in range(int(input())):
        tmp = int(input())

        if tmp == 4:
            print(1)
        else:
            print((int(round(oddPrime[(tmp-2)//2].real))+1)//2)

    return


if __name__ == "__main__":
    main()