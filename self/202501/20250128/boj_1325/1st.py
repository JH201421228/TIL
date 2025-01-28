import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n):
    V[n] = 1
    S.append(n)
    ans = 1

    while S:
        o = S.pop()
        for x in G[o]:
            if not V[x]:
                ans += 1
                V[x] = 1
                S.append(x)

    return ans



N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
V = [0] * (N+1)
S = []

for _ in range(M):
    u, v = map(int, input().split())
    G[v].append(u)

ans_list = []
for n in range(1, N+1):
    V = [0] * (N+1)
    ans_list.append(dfs(n))

max_v = max(ans_list)
ans = [i+1 for i in range(N) if ans_list[i] == max_v]
print(*ans)
