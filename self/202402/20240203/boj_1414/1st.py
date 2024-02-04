import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
graph = []
total = 0
for i in range(N):
    temp = list(input().rstrip())
    for j in range(N):
        if temp[j] == '0':
            continue
        elif temp[j] >= 'a':
            total += (ord(temp[j]) - ord('a') + 1)
            if i != j:
                graph.append((i, j, (ord(temp[j]) - ord('a') + 1)))
        else:
            total += (ord(temp[j]) - ord('A') + 27)
            if i != j:
                graph.append((i, j, (ord(temp[j]) - ord('A') + 27)))

graph.sort(key=lambda x: x[2])

parent = [i for i in range(N)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = parent[x]
    y = parent[y]
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def same_parent(x, y):
    return find_parent(x) == find_parent(y)


ans = 0
check = 0
for a, b, c in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        ans += c
        check += 1
if check == N-1:
    print(total - ans)
else:
    print(-1)
