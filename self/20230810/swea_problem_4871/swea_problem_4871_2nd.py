import sys
sys.stdin = open('input.txt')


def DFS(node, V):
    tarace[node] = 1

    for next in range(1, V+1):
        if not tarace[next] and matrix[node][next]:
            ans.append(next)
            DFS(next, V)
    return ans

Test_Case = int(input())

for test_case in range(Test_Case):
    V, E = list(map(int, input().split()))
    matrix = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        matrix[start][end] = 1

    start_num, end_num = map(int, input().split())
    tarace = [0] * (V+1)
    ans = [start_num]
    if end_num in DFS(start_num, V):
        print(f'#{test_case + 1} 1')
    else:
        print(f'#{test_case + 1} 0')
