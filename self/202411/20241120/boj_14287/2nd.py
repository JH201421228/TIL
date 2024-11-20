import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline

def dfs(n):
    global cnt
    A[n] = cnt = cnt+1
    for x in G[n]:
        dfs(x)
    E[n] = cnt

def U(idx, v):
    while idx < N+1:
        T[idx] += v
        idx += (idx & -idx)

def S(idx):
    ans = 0
    while idx > 0:
        ans += T[idx]
        idx -= (idx & -idx)
    return ans

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
A = [0] * (N+1)
E = [0] * (N+1)
cnt = 0

temp = list(map(int, input().split()))
for i in range(1, N):
    G[temp[i]].append(i+1)

dfs(1)
T = [0] * (cnt+1)

for _ in range(M):
    temp = list(map(int, input().split()))

    if temp[0] == 1:
        U(A[temp[1]], temp[2])
    else:
        print(S(E[temp[1]]) - S(A[temp[1]]-1))