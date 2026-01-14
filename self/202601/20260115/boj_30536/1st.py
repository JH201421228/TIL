import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    
    if N == M:
        print(0)
        return
    
    X, Y = [0], [0]
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
        
    P = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    dist = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            dist[i][j] = dist[j][i] = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**.5
    
    V = [0] * (N+1)
    for p in P: V[p] = -1
    
    q = deque([])
    ans = 0
    
    for i in range(N+1):
        if V[i]: continue
        
        for idx in range(M):
            j = P[idx]
            if dist[i][j] <= R[idx+1]: break
        else:
            V[i] = 1
            q.append(i)
            ans += 1
            
    while q:
        n = q.popleft()
        
        for x in range(1, N+1):
            if x != n and V[x] != 1 and dist[n][x] <= R[0]:
                V[x] = 1
                ans += 1
                q.append(x)

    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()