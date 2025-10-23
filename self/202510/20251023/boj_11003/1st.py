import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, L = map(int, input().split())

    arr = list(map(int, input().split()))

    q = deque([])

    D = []

    for idx in range(N):
        if not q:
            q.append((arr[idx], idx))
        else:
            if idx - q[0][1] >= L:
                q.popleft()

            cur = arr[idx]

            while q and q[-1][0] > cur:
                q.pop()

            q.append((arr[idx], idx))

        D.append(q[0][0])

    print(*D)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()