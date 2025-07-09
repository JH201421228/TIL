import sys
from typing import List
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(n, k, i, j):
    global arr

    if k == arr[n-1] + 1:
        return i, j
    elif k > arr[n-1] + 1:
        return find(n-1, k - arr[n-1] - 1, 6 - i - j, j)
    else:
        return find(n-1, k, i, 6 - i - j)


def solve():
    global arr

    N, K = map(int, input().split())
    arr = [2**n - 1 for n in range(N+1)]

    print(*find(N, K, 1, 3))

    return


if __name__ == "__main__":
    arr: List[int]
    N: int
    K: int
    solve()