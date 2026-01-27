import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dia = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def bfs(N, M):
    grid = [list(map(int, input().split())) for _ in range(N)]
    cur = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
    cand = []
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 1: cand.append([i, j])
    
    for _ in range(M):
        d, s = map(int, input().split())
        V = [[0] * N for _ in range(N)]

        for idx in range(len(cur)):
            cur[idx][0] = (cur[idx][0] + s * delta[d-1][0]) % N
            cur[idx][1] = (cur[idx][1] + s * delta[d-1][1]) % N
            
        for i, j in cur:
            grid[i][j] += 1
            V[i][j] = 1
            
        for i, j in cur:
            for di, dj in dia:
                ii, jj = i+di, j+dj
                if ii >= 0 and ii < N and jj >= 0 and jj < N and grid[ii][jj]:
                    grid[i][j] += 1
            if grid[i][j] > 1: cand.append([i, j])
        
        temp = []
        cur = []
        while cand:
            i, j = cand.pop()
            if grid[i][j] > 1:
                if not V[i][j]:
                    V[i][j] = 1
                    grid[i][j] -= 2
                    cur.append([i, j])
                    if grid[i][j] > 1: temp.append([i, j])
                else:
                    temp.append([i, j])
                    
        cand = temp
          
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