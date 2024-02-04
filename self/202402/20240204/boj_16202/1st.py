import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
graph = []
for i in range(M):
    temp = list(map(int, input().split()))
    temp.append(i+1)
    graph.append(temp)
print(graph)