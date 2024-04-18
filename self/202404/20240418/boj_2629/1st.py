import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


weight_n = int(input())
weights = list(map(int, input().split()))
ball_n = int(input())
balls = list(map(int, input().split()))

max_val = sum(weights) if sum(weights) < 40_001 else 40_000

graph = [[0] * (max_val + 1) for _ in range(weight_n)]

graph[0][0], graph[0][weights[0]] = 1, 1

for i in range(weight_n-1):
    for j in range(max_val+1):
        if graph[i][j]:
            graph[i+1][j], graph[i+1][j+weights[i+1]], graph[i+1][abs(j-weights[i+1])] = 1, 1, 1
ans = []
for val in balls:
    if val <= max_val and graph[-1][val]:
        ans.append('Y')
    else:
        ans.append('N')
print(*ans)