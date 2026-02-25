import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    
    h, w = map(int, input().split())
    
    road = [list(map(int, input().split())) for _ in range(N)]
    
    K = int(input())
    q = deque([tuple(map(int, input().split())) for _ in range(K)])
    
    V = [[0] * M for _ in range(N)]
    
    for x, y in q: V[x-1][y-1] = 1
    
    delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            if xx > 0 and xx <= N and yy > 0 and yy <= M and not V[xx-1][yy-1] and road[xx-1][yy-1] >= road[x-1][y-1]:
                V[xx-1][yy-1] = 1
                q.append((xx, yy))
    
    boot = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        boot
        for j in range(1, M+1):
            if V[i-1][j-1]: boot[i][j] = 1
            boot[i][j] += boot[i][j-1] + boot[i-1][j] - boot[i-1][j-1]
        
    ans = 0
        
    for i in range(h, N+1):
        for j in range(w, M+1):
            area = boot[i][j] + boot[i-h][j-w] - boot[i-h][j] - boot[i][j-w]
            if area == h*w: ans += 1
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()