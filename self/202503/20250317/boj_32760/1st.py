import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

G = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = []
least = 0
isPossible = True
for idx in range(N, 1, -1):
    if len(G[idx]) == idx - 1 + least:
        least += 1
        ans.append('E')
    elif not G[idx]:
        ans.append('N')
    else:
        isPossible = False

    if not isPossible:
        print(-1)
        exit(0)

while ans:
    print(ans.pop(), end='')