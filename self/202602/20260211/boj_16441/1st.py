import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(q, field, V, N, M):
    
    while q:
        i, j = q.popleft()
        for di, dj in delta:
            ii, jj = i+di, j+dj
            
            if ii >= 0 and ii < N and jj >= 0 and jj < M and not V[ii][jj] and field[ii][jj] != "#":
                if field[ii][jj] == ".":
                    q.append((ii, jj))
                    V[ii][jj] = 1
                    
                else:
                    while True:
                        ii, jj = ii+di, jj+dj
                        if field[ii][jj] == "#":
                            if not V[ii-di][jj-dj]:
                                V[ii-di][jj-dj] = 1
                                q.append((ii-di, jj-dj))
                            break
                        elif field[ii][jj] == "." and not V[ii][jj]:
                            V[ii][jj] = 1
                            q.append((ii, jj))
                            break
    
    return V


def solve():
    N, M = map(int, input().split())
    field = [list(input().rstrip()) for _ in range(N)]
    
    q = deque([])
    V = [[0] * M for _ in range(N)]
    
    wolf = []
    
    for i in range(N):
        for j in range(M):
            if field[i][j] == "W":
                field[i][j] = "."
                q.append((i, j))
                wolf.append((i, j))
                V[i][j] = 1
    
    
    V = bfs(q, field, V, N, M)
    
    for i in range(N):
        for j in range(M):
            if not V[i][j] and field[i][j] == '.':
                field[i][j] = 'P'
    
    for i, j in wolf:
        field[i][j] = 'W'
        
    for f in field:
        print(''.join(f))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()