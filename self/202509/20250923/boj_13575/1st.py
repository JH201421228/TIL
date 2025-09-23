import sys
import math
sys.stdin.readline('input.txt')
input = sys.stdin.readline


PI = math.pi


def dq():
    return


def fft(v, inv):
    N = len(v)

    j = 0
    for i in range(1, N):
        b = N >> 1
        while j&b:
            j ^= b
            b >>= 1
        j ^= b

        if i < j:
            v[i], v[j] = v[j], v[i]

    k = 1
    while k < N:
        a = (PI/k) if inv else -(PI/k)
        w = complex(math.cos(a), math.sin(a))

        for i in range(0, N, k<<1):
            wp = 1+0j
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
    N = len(u)

    fft(u, False)

    # for i in range(N)

    fft(u, True)

    return


def solve():
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()