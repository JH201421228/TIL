import sys
from collections import deque
input = sys.stdin.readline

LOG = 18

def solve():
    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split())) 
    
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    parent = [[0] * LOG for _ in range(N+1)]
    depth = [-1] * (N+1)
    
    queue = deque([1]) # 루트를 1번으로 가정
    depth[1] = 0
    
    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if depth[nxt] == -1:
                depth[nxt] = depth[cur] + 1
                parent[nxt][0] = cur
                queue.append(nxt)
    
    for i in range(1, LOG):
        for j in range(1, N+1):
            if parent[j][i-1] != 0:
                parent[j][i] = parent[parent[j][i-1]][i-1]

    # LCA 함수
    def get_lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        
        # 깊이 맞추기
        for i in range(LOG-1, -1, -1):
            if depth[a] - depth[b] >= (1 << i):
                a = parent[a][i]
        
        if a == b:
            return a
            
        # 공통 조상 바로 아래까지 올리기
        for i in range(LOG-1, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
                
        return parent[a][0]

    MOD = 1_000_000_007
    result = []

    for _ in range(Q):
        x, y = map(int, input().split())
        lca = get_lca(x, y)
        
        # 경로 복원: x -> ... -> lca -> ... -> y
        # 주의: 이 부분도 경로가 길면 O(N)이라 느릴 수 있음.
        # 문제 특성상 "경로의 값 계산"을 O(log N)으로 하려면 
        # prefix sum 등의 추가 테크닉이 필요할 수 있으나,
        # 일단 경로 탐색 자체를 최적화하여 구현합니다.
        
        path_x_to_lca = []
        cur = x
        while cur != lca:
            path_x_to_lca.append(cur)
            cur = parent[cur][0]
        path_x_to_lca.append(lca)
        
        path_y_to_lca = []
        cur = y
        while cur != lca:
            path_y_to_lca.append(cur)
            cur = parent[cur][0]
        
        # 전체 경로 합치기 (x -> lca ... lca -> y 역순)
        full_path = path_x_to_lca + path_y_to_lca[::-1]
        
        # 값 계산 로직 최적화
        tmp = 0
        l_sum = 0
        
        # full_path는 [start_node, ... , end_node] 순서
        # 문제는 "뒤에서부터(end_node)" 자릿수를 더해가는 로직이므로 reverse 해서 처리
        # 작성하신 로직: ans 리스트의 뒤에서부터 1의 자리, 10의 자리... 
        
        for node in reversed(full_path):
            val = A[node]
            # 파이썬 pow(base, exp, mod)는 매우 빠름
            term = (val * pow(10, l_sum, MOD)) % MOD
            tmp = (tmp + term) % MOD
            l_sum += len(str(val)) # 숫자의 길이만큼 자릿수 증가
            
        result.append(str(tmp))

    print("\n".join(result))

if __name__ == "__main__":
    solve()