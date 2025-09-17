import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi


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


def fft_wrapper(u, v, n):
    N = len(u)

    fft(u, False)

    for i in range(N):
        u[i] *= u[i]

    fft(u, True)

    ans = 0

    for i in range(N):
        tmp = round(u[i].real)
        if tmp and v[i%n]:
            if i % 2:
                ans += (tmp//2) * v[i%n]
            else:
                ans += ((tmp-v[i//2])//2 + v[i//2]) * v[i%n]

    print(ans)

    return


def solve(N):
    M = 1
    while M < N:
        M <<= 1
    M <<= 1

    u = [0] * M
    v = [0] * M

    for i in range(1, N):
        u[(i*i)%N] += 1
        v[(i*i)%N] += 1

    fft_wrapper(u, v, N)

    return


def main():
    solve(int(input()))
    return


if __name__ == "__main__":
    main()