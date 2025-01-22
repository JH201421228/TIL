import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
C = []
max_x, max_y, min_x, min_y = -float("inf"), -float("inf"), float("inf"), float("inf")
for _ in range(N):
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    min_x = min(min_x, x)
    min_y = min(min_y, y)

    C.append((x, y))

len_x, len_y = max_x-min_x, max_y-min_y

if len_x != len_y:
    if len_x > len_y:
        L = [[(max_x, min_x), (min_y+len_x, min_y)], [(max_x, min_x), (max_y, max_y-len_x)]]
    else:
        L = [[(min_x+len_y, min_x), (max_y, min_y)], [(max_x, max_x-len_y), (max_y, min_y)]]
else:
    L = [[(max_x, min_x), (max_y, min_y)]]

for X, Y in L:
    for x, y in C:
        if x in X or y in Y:
            continue
        else:
            break
    else:
        print(max(len_x, len_y))
        exit(0)

print(-1)