import sys
from pprint import pprint as pprint
sys.stdin = open('input.txt')

def DFS(node, V):
    trace = [0] * (V+1) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stack = [node]
    trace[node] = 1 # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    stack = [node]
    ans = [node]
    while stack:
        start = stack.pop()
        for next in range(1, V+1):
            if not trace[next] and matrix[start][next]:
                stack.append(next)
                trace[next] = 1
                ans.append(next)
    return ans

Test_Case = int(input())

for test_case in range(Test_Case):
    V, E = map(int, input().split())
    matrix = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        matrix[start][end] = 1
    start_num, end_num = map(int, input().split())

    if end_num in DFS(start_num, V):
        print(f'#{test_case + 1} 1')
    else:
        print(f'#{test_case + 1} 0')
