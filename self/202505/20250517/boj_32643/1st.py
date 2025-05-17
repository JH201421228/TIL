import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    sieve = [1] * (N+1)
    sieve[0] = 0

    for n in range(2, int(N**.5)+1):
        if sieve[n]:
            for m in range(n**2, N+1, n): sieve[m] = 0

    for idx in range(2, N+1):
        sieve[idx] += sieve[idx-1]

    for _ in range(M):
        a, b = map(int, input().split())
        print(sieve[b]-sieve[a-1])

    return


if __name__ == "__main__":
    solve()