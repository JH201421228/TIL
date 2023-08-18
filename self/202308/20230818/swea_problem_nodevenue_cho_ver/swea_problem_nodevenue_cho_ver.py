import sys
sys.stdin = open('input.txt')

def bfs(s, v):
    # visited = [0] * (v+1) # 함수 밖으로 옮김
    que = []
    que.append(s)
    visited[s] = 1
    # cnt = 0
    # low_length = 0

    while que:
        now = que.pop(0)

        # for w in matrix[t]:
        # if visited[t] == 0: 이미 visited[s] = 1 를 했기 때문에 visited[t] == 0 는 항상 False임
        #     visited[t] = 1
            # cnt += 1
        for next in range(1, V+1): # range(1, v+1)
            if not visited[next] and matrix[now][next]: # visited[t] 를 visited[next] 로 변경, matrix[t][next] == 0 을 matrix[t][next] == 1로 변경
                if next == v:
                    visited[next] = visited[now] + 1
                    return visited[now]
                que.append(next) # que.append(t) 를 que.append(next)로 변경
                visited[next] = visited[now] + 1


        # if low_length >= cnt:
        #     low_length = cnt
    return 0


T = int(input())

for tc in range(1, T+1):
    # V = 노드 개수, E = 간선 개수(방향성 없음)
    V, E = map(int, input().split())
    matrix = [[0]*(V+1) for _ in range(V+1)]
    for t in range(E):  # E개의 줄에 걸쳐서
        # 간선 양쪽 노드 정보 v1, v2 주어짐
        v1, v2 = map(int, input().split())
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1
    S, G = map(int, input().split())
    visited = [0] * (V + 1)

    # print(matrix)
    if bfs(S, G):
        print(visited[G])
    else:
        print()
