import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100_000)
input = sys.stdin.readline


def makeTree(n, p):
    S[n] = 1

    for x in arr[n]:
        if x != p:
            P[x] = n
            makeTree(x, n)
            S[n] += S[x]


N, R, Q = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

P = [i for i in range(N+1)]
S = [0] * (N+1)

makeTree(R, R)

for _ in range(Q):
    print(S[int(input())])