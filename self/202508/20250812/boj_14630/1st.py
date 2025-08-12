import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def charge(pre, nxt):
    total = 0
    length = len(pre)
    for idx in range(length):
        total += (int(pre[idx])-int(nxt[idx]))**2

    return total


def solve():
    N = int(input())
    states = [input().rstrip() for _ in range(N)]
    s, e = map(int, input().split())
    V = [float("inf")] * N
    V[s-1] = 0
    q = deque([(s-1, 0)])

    while q:
        n, dist = q.popleft()

        for x in range(N):
            c = charge(states[n], states[x])

            if c+dist < V[x]:
                V[x] = c+dist
                q.append((x, V[x]))

    print(V[e-1])

    return


if __name__ == "__main__":
    solve()