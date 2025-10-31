import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, D = map(int, input().split())
    K = list(map(int, input().split()))

    q = deque([])
    ans = 0

    for idx in range(N):
        cur = K[idx] if not q else q[0][0] + K[idx]

        cur = cur if cur > 0 else 0

        ans = max(cur, ans)


        while q and idx - q[0][1] >= D:
            q.popleft()
        
        while q and q[-1][0] <= cur:
            q.pop()

        q.append((cur, idx))

    print(ans if ans > 0 else max(K))

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()