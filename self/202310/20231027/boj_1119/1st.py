import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 도시 수 - 1 보다 길의 수가 많으면
# 그룹 수를 측정
# 그룹수 -1이 답
# 도시 수 - 1 보다 길의 수가 작으면 절대 못 이음


def why(idx):
    check = 1
    for i in range(N):
        if not visited[i] and graph[idx][i]:
            visited[i] = 1
            check += why(i)
    return check


trans = {'Y':1, 'N':0}

N = int(input())

if N == 1:
    print(0)
    exit(0)

graph = [list(input().rstrip()) for _ in range(N)]
cnt = 0 # 도로의 수

for i in range(N):
    for j in range(i, N):
        if i == j:
            graph[i][i] = 0
        else:
            graph[i][j] = graph[j][i] = trans[graph[i][j]]
            if graph[i][j]:
                cnt += 1

visited = [0] * N
group_num = 0
for i in range(N):
    if not visited[i]:
        visited[i] = 1
        if why(i) == 1:
            print(-1)
            exit(0)
        group_num += 1

if not cnt:
    print(-1)
elif cnt >= N-1:
    print(group_num - 1)
else:
    print(-1)