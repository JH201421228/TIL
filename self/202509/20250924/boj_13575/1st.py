import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline


PI = math.pi


def dq(N, v):
    if N == 1:
        return v
    
    u = dq(N//2, v)
    w = dq(N-N//2, v)

    res = []
    for a, b in zip(u, w):
        res.append(a*b)

    return res


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


def fft_wrapper(u, K):
    N = len(u)

    fft(u, False)

    u = dq(K, u)

    fft(u, True)

    ans = []
    for idx in range(N):
        if round(u[idx].real) > 0:
            ans.append(idx)

    ans.sort()
    print(*ans)

    return


def solve(N, K):
    temp = list(map(int, input().split()))

    u = [0j] * (1<<20)
    for t in temp:
        u[t] = 1+0j

    fft_wrapper(u, K)

    return


def main():
    N, K = map(int, input().split())
    solve(N, K)

    return


if __name__ == "__main__":
    main()