import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10_000)
input = sys.stdin.readline


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])

    return p[x]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b
    return


def solve():
    N, M = map(int, input().split())

    priorities = list(map(int, input().split()))
    priorities_dict = {priorities[idx]: idx for idx in range(3)}

    G = []

    for _ in range(M):
        u, v, w, k = map(int, input().split())

        G.append((w, priorities_dict[k], u, v))

    G.sort()

    ans = [0, [0, 0], [0, 0], [0, 0]]
    idx = 0
    cnt = 0
    p = [i for i in range(N+1)]
    while G:
        w, pr, u, v = G[idx]

        if find_parent(p, u) != find_parent(p, v):
            union_parent(p, u, v)
            ans[0] += w
            ans[priorities[pr]+1][0] += 1
            ans[priorities[pr]+1][1] += w
            cnt += 1

        if cnt == N-1: break

        idx += 1

    print(ans[0])
    for _ in ans[1:]:
        print(*_)

    return


if __name__ == "__main__":
    solve()