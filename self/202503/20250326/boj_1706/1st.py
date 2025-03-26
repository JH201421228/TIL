import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


R, C = map(int, input().split())
P = [list(input().rstrip()) for _ in range(R)]

W = []
for i in range(R):
    n = ''
    for j in range(C):
        if P[i][j] == '#':
            if n and len(n) > 1:
                W.append(n)
            n = ''
        else:
            n += P[i][j]
    if n and len(n) > 1:
        W.append(n)

for j in range(C):
    n = ''
    for i in range(R):
        if P[i][j] == '#':
            if n and len(n) > 1:
                W.append(n)
            n = ''
        else:
            n += P[i][j]
    if n and len(n) > 1:
        W.append(n)

W.sort()
print(W[0])