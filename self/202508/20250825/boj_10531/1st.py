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
        while (j ^ b) < j:
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
                v[i+j] = x+y
                v[i+j+k] = x-y
                wp *= w

        k <<= 1

    if inv:
        inv_n = 1.0/n
        for i in range(n):
            v[i] *= inv_n

    return


def fft_start(v):
    n = 1

    length = len(v)
    while n <= length:
        n <<= 1
    n <<= 1

    v.extend([0j] * (n - length))

    fft(v, False)
    for i in range(n):
        v[i] = v[i]*v[i]

    fft(v, True)

    return


def solve():
    N = int(input())
    shot = [int(input()) for _ in range(N)]

    M = int(input())
    distance = [int(input()) for _ in range(M)]

    v = [0j] * (max(shot)+1)
    v[0] = 1+0j
    for n in shot:
        v[n] = 1+0j

    fft_start(v)

    ans = 0
    L = len(v)
    for dist in distance:
        if dist < L and round(v[dist].real) > 0:
            ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()