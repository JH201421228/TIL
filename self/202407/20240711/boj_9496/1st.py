import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(G, n):
    for x in G[n]:
        if V[x]:
            continue

        V[x] = 1

        if not C[x] or B(G, C[x]):
            C[x] = n
            return True

    return False


N = int(input())
grades = list(map(int, map(str, input().rstrip())))
relation = []
for _ in range(N):
    relation.append(list(map(str, input().rstrip())))

G12, G13, G23 = [[] for _ in range(N+1)], [[] for _ in range(N+1)], [[] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue

        if grades[i-1] == 1:
            if grades[j-1] == 2 and relation[i-1][j-1] == 'Y':
                G12[i].append(j)
            elif grades[j-1] == 3 and relation[i-1][j-1] == 'Y':
                G13[i].append(j)

        elif grades[i-1] == 2 and grades[j-1] == 3 and relation[i-1][j-1] == 'Y':
            G23[i].append(j)

cnt = []

C = [0] * (N+1)
val = 0
for i in range(1, N+1):
    V = [0] * (N+1)
    if B(G12, i):
        val += 1

cnt.append(val)

C = [0] * (N+1)
val = 0
for i in range(1, N+1):
    V = [0] * (N+1)
    if B(G13, i):
        val += 1

cnt.append(val)

C = [0] * (N+1)
val = 0
for i in range(1, N+1):
    V = [0] * (N+1)
    if B(G23, i):
        val += 1

cnt.append(val)

print(N-min(cnt))