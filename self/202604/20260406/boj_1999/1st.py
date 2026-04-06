import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, B, K = map(int, input().split())
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    M = N-B+1
    
    row_max = [[0] * M for _ in range(N)]
    row_min = [[0] * M for _ in range(N)]
    
    for i in range(N):
        dq_max = deque()
        dq_min = deque()
        
        for j in range(N):
            while dq_max and arr[i][dq_max[-1]] <= arr[i][j]: dq_max.pop()
            dq_max.append(j)
            
            while dq_min and arr[i][dq_min[-1]] >= arr[i][j]: dq_min.pop()
            dq_min.append(j)
            
            while dq_max and dq_max[0] <= j-B: dq_max.popleft()
            while dq_min and dq_min[0] <= j-B: dq_min.popleft()
            
            if j >= B-1:
                s = j-B+1
                row_max[i][s] = arr[i][dq_max[0]]
                row_min[i][s] = arr[i][dq_min[0]]
                
    box_max = [[0] * M for _ in range(M)]
    box_min = [[0] * M for _ in range(M)]
    
    for j in range(M):
        dq_max = deque()
        dq_min = deque()
        
        for i in range(N):
            while dq_max and row_max[dq_max[-1]][j] <= row_max[i][j]: dq_max.pop()
            dq_max.append(i)
            
            while dq_min and row_min[dq_min[-1]][j] >= row_min[i][j]: dq_min.pop()
            dq_min.append(i)
            
            while dq_max and dq_max[0] <= i-B: dq_max.popleft()
            while dq_min and dq_min[0] <= i-B: dq_min.popleft()
            
            if i >= B-1:
                s = i-B+1
                box_max[s][j] = row_max[dq_max[0]][j]
                box_min[s][j] = row_min[dq_min[0]][j]
            
    for _ in range(K):
        i, j = map(int, input().split())
        
        print(box_max[i-1][j-1] - box_min[i-1][j-1])
            
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()