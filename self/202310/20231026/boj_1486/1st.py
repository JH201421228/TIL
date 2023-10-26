import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(val, time, i, j):
    global ans

    if time > D:
        return

    if time <= D and val > ans:
        ans = val


    for di, dj in delta:
        if 0 <= i+di < N and 0 <= j+dj <M and not visited[i+di][j+dj]:
            if abs(mountain[i+di][j+dj] - mountain[i][j]) > T:
                continue
            visited[i+di][j+dj] = 1
            if mountain[i+di][j+dj] > mountain[i][j]:
                dfs(mountain[i+di][j+dj], time + (mountain[i+di][j+dj] - mountain[i][j])**2, i+di, j+dj)
            else:
                dfs(mountain[i+di][j+dj], time + 1, i+di, j+dj)
            visited[i+di][j+dj] = 0





N, M, T, D = map(int, input().split())
mountain = [list(input().rstrip()) for _ in range(N)]
# print(mountain)
for i in range(N):
    for j in range(M):
        num = ord(mountain[i][j]) - ord('A')
        if num > 25:
            num -= 6
        mountain[i][j] = num

for inner in mountain:
    print(inner)

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
ans = 0
dfs(mountain[0][0], 0, 0, 0)
print(ans)
