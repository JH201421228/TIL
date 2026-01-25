import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
nums = {
    0: [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    1: [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    2: [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    3: [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    4: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    5: [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    6: [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    8: [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
}

def bfs(i, j, N, M, asterisks):
    q = deque([(i, j)])
    bag = [(i, j)]
    asterisks[i][j] = " "
    
    while q:
        ni, nj = q.popleft()
        for di, dj in delta:
            ii, jj = ni+di, nj+dj
            if ii >= 0 and ii < N and jj >= 0 and jj < M and asterisks[ii][jj] == "*":
                asterisks[ii][jj] = " "
                q.append((ii, jj))
                bag.append((ii, jj))
    
    return bag


def find_ans(bag):
    bag.sort()
    
    k = (bag[-1][0] - bag[0][0] + 1) // 5
    temp = [[0] * 3*k for _ in range(5*k)]
    
    oi, oj = float("inf"), float("inf")
    for i, j in bag:
        oi = min(oi, i)
        oj = min(oj, j)
    for i, j in bag: temp[i-oi][j-oj] = 1
    
    num = []
    for i in range(0, 5*k, k):
        for j in range(0, 3*k, k):
            if temp[i][j]: num.append(1)
            else: num.append(0)
            
    for k, v in nums.items():
        if v == num:
            print(k)
            return
        
    return 


def solve():
    N, M = map(int, input().split())
    asterisks = [list(input().rstrip().ljust(M, " ")) for _ in range(N)]
    
    bag = []
    cur_size = 0
    for i in range(N):
        for j in range(M):
            if asterisks[i][j] == "*":
                temp_bag = bfs(i, j, N, M, asterisks)
                min_i, max_i  = float("inf"), 0
                for i, _ in temp_bag:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                nxt_size = max_i - min_i
                if nxt_size > cur_size:
                    cur_size = nxt_size
                    bag = temp_bag
            
    find_ans(bag)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()