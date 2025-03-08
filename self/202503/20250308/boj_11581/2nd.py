import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def detect_cycle(n, graph):
    visited = [False] * (n + 1)  # 노드 방문 여부
    on_stack = [False] * (n + 1)  # 현재 탐색 중인 경로에 포함된 노드 여부

    def dfs(node):
        visited[node] = True
        on_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:  # 방문하지 않은 노드라면 DFS 탐색
                if dfs(neighbor):
                    return True
            elif on_stack[neighbor]:  # 현재 경로에서 다시 만난다면 사이클 존재
                return True

        on_stack[node] = False  # 탐색이 끝난 노드 제거
        return False

    # 1번 노드에서 시작하여 DFS 탐색
    if dfs(1):
        return "CYCLE"
    return "NO CYCLE"


# 입력 처리
n = int(input().strip())  # 교차로의 수
graph = {i: [] for i in range(1, n + 1)}

for i in range(1, n):  # 1번부터 N-1번 교차로까지 입력 받기
    m = int(input().strip())  # 연결된 교차로의 개수

    connections = list(map(int, input().strip().split()))
    graph[i].extend(connections)

# 결과 출력
print(detect_cycle(n, graph))
