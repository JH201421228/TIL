import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi


def fft(v, inv):
    n = len(v)

    j = 0
    for i in range(1, n):
        b = n >> 1
        while j & b:
            j ^= b
            b >>= 1
        j ^= b

        if i < j:
            v[i], v[j] = v[j], v[i]

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

    res = [0j] * n

    fft(v, False)
    fft(u, False)

    for i in range(n):
        res[i] = u[i] * v[i]

    fft(res, True)

    ans = 0

    for idx in range(n-1, -1, -1):
        ans = max(ans, round(res[idx].real))

    print(ans)

    return


def solve():
    N = int(input())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    u += u
    for idx in range(N//2):
        v[idx], v[N-idx-1] = v[N-idx-1], v[idx]

    fft_wrapper(u, v)

    return


if __name__ == "__main__":
    solve()