import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def check_map(N, M, maps):
    res = [[0] * M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] and not res[i][j]:
                cnt += 1

                q = deque([(i, j)])
                res[i][j] = cnt

                while q:
                    x, y = q.popleft()

                    for dx, dy in delta:
                        xx, yy = x+dx, y+dy
                        
                        if xx >= 0 and xx < N and yy >= 0 and yy < M and not res[xx][yy] and maps[xx][yy]:
                            res[xx][yy] = cnt
                            q.append((xx, yy))

    return res, cnt


def check_graph(N, M, cur_map):
    res = []

    for i in range(N):
        cur = 0
        length = 0

        for j in range(M):
            if not cur_map[i][j]: length += 1
            else:
                if cur and length > 1:
                    heapq.heappush(res, (length, cur, cur_map[i][j]))
                length = 0
                cur = cur_map[i][j]

    for j in range(M):
        cur = 0
        length = 0

        for i in range(N):
            if not cur_map[i][j]: length += 1
            else:
                if cur and length > 1:
                    heapq.heappush(res, (length, cur, cur_map[i][j]))
                length = 0
                cur = cur_map[i][j]
                
    return res


def find_parent(n, parent):
    if parent[n] == n: return n
    return find_parent(parent[n], parent)


def union_find(a, b, parent):
    a_p = find_parent(a, parent)
    b_p = find_parent(b, parent)

    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

    return


def solve():
    N, M = map(int, input().split())

    maps = [list(map(int, input().split())) for _ in range(N)]

    cur_map, cnt = check_map(N, M, maps)

    graph = check_graph(N, M, cur_map)

    parent = [i for i in range(cnt+1)]

    ans = 0

    while graph:
        d, a, b = heapq.heappop(graph)

        if find_parent(a, parent) == find_parent(b, parent):
            continue

        union_find(a, b, parent)

        ans += d
        cnt -= 1

    if cnt == 1:
        print(ans)
    else:
        print(-1)


    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()