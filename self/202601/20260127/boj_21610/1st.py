import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dia = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def bfs(N, M):
    grid = [list(map(int, input().split())) for _ in range(N)]
    cur = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    
    for _ in range(M):
        d, s = map(int, input().split())

        for idx in range(len(cur)):
            cur[idx][0] = (cur[idx][0] + s * delta[d-1][0]) % N
            cur[idx][1] = (cur[idx][1] + s * delta[d-1][1]) % N
            
        for i, j in cur:
            grid[i][j] += 1
            
        for i, j in cur:
            for di, dj in dia:
                ii, jj = i+di, j+dj
                if ii >= 0 and ii < N and jj >= 0 and jj < N and grid[ii][jj]: grid[i][j] += 1
                
        prev_set = set((i, j) for i, j in cur)
        cur = []

        for i in range(N):
            for j in range(N):
                if grid[i][j] > 1 and (i, j) not in prev_set:
                    grid[i][j] -= 2
                    cur.append([i, j])
                
    ans = 0
    for i in range(N):
        for j in range(N): ans += grid[i][j]
                 
    return ans


def solve():
    N, M = map(int, input().split())
    
    print(bfs(N, M))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()