import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False

R, C = map(int, input().split())

M = [list(map(str, input().rstrip())) for _ in range(R)]
x_s = [tuple()]
cnt = 0
cur = False # 현재 도시가 아니다
name = ['']
temp = ''

for i in range(R):
    if cur:
        name.append(temp)
        temp = ''
        cur = False

    for j in range(C):
        if M[i][j] == '.':
            if cur:
                name.append(temp)
                temp = ''
                cur = False

        elif M[i][j] == 'x':
            x_s.append((i, j))
            if cur:
                name.append(temp)
                temp = ''
                cur = False

        else:
            if not cur:
                cnt += 1
            temp += M[i][j]
            M[i][j] = cnt
            cur = True

if temp:
    name.append(temp)

delta = [(1, 1), (1, 0), (1, -1), (0, 1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]

cities = len(x_s)

G = [[] for _ in range(cities+1)]

for i in range(1, cities):
    x, y = x_s[i]
    for dx, dy in delta:
        if x+dx >= 0 and x+dx < R and y+dy >= 0 and y+dy < C:
            if M[x+dx][y+dy] not in ['.', 'x'] and M[x+dx][y+dy] not in G[i]:
                G[i].append(M[x+dx][y+dy])

C = [0] * (cnt+1)

# print(cnt, cities)

for i in range(1, cities):
    V = [0] * (cnt+1)
    B(i)

# print(len(name))
# print(len(x_s))
# print(C)

for i in range(cnt):
    print(x_s[C[i+1]][0] + 1, x_s[C[i+1]][1] + 1, name[i+1])

# print(G)
# for inner in M:
#     print(inner)

