import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi


def fft(v, inv):
    n = len(v)

    j = 0
    for i in range(1, n):
        b = n>>1
        while j&b:
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
            wp = 1+0j
            for j in range(k):
                x = v[i+j]
                y = v[i+j+k] * wp

                v[i+j] = x+y
                v[i+j+k] = x-y

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

    u.extend([0j] * (n-length))
    v.extend([0j] * (n-len(v)))

    fft(u, False)
    fft(v, False)

    for i in range(n):
        u[i] = u[i]*v[i]

    fft(u, True)

    ans = 0

    for i in range(n):
        ans = max(ans, round(u[i].real))

    print(ans)

    return


def solve():
    u = list(map(int, input().rstrip()))
    v = list(map(int, input().rstrip()))

    u += u
    v

    length = len(v)

    for i in range(length//2):
        v[i], v[length-1-i] = v[length-1-i], v[i]

    fft_wrapper(u, v)

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()