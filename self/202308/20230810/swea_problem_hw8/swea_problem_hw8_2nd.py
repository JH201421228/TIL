import sys
sys.stdin = open('input.txt')


def DFS(num):
    trace[num] = 1

    for next in range(100):
        if not trace[next] and matrix[num][next]:
            ans.append(next)
            DFS(next)
    return ans


for _ in range(10):
    tc, E = map(int, input().split())
    matrix = [[0] * 100 for _ in range(100)]
    mapping_list = list(map(int, input().split()))

    for i in range(E):
        matrix[mapping_list[2*i]][mapping_list[2*i + 1]] = 1

    ans = [0]
    trace = [0] * 100
    if 99 in DFS(0):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')