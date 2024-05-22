from collections import deque

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

def solution(land):
    answer = 0

    def bfs(x, y):
        visited[x][y] = 1
        check_set = set()
        check_set.add(y)
        q = deque([(x, y)])
        val = 1
        while q:
            x, y = q.popleft()
            for dx, dy in delta:
                if 0 <= x + dx < n and 0 <= y + dy < m and not visited[x + dx][y + dy] and land[x + dx][y + dy]:
                    q.append((x + dx, y + dy))
                    val += 1
                    visited[x + dx][y + dy] = 1
                    check_set.add(y + dy)
        for idx in check_set:
            check_dict[idx] = check_dict.get(idx, 0) + val
        return val

    n = len(land)
    m = len(land[0])
    check_dict = dict()

    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                bfs(i, j)

    for key, value in check_dict.items():
        if value > answer:
            answer = value
    return answer

print(solution(land))