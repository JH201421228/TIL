import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    arr = [float(input()) for _ in range(N)]
    arr.sort()
    arr = [arr[K]]*K + arr[K:N-K] + [arr[-1-K]]*K

    correction = 1e-8

    print(f"{sum(arr[K:N - K]) / (N - 2 * K) + correction:.2f}")
    print(f"{sum(arr)/N + correction:.2f}")

    return


if __name__ == "__main__":
    solve()