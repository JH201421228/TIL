import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    cur = list(map(int, list(input().rstrip())))
    tar = list(map(int, list(input().rstrip())))
    
    
    dp = [[float("inf")] * 10 for _ in range(N+1)]
    trace = [[0] * 10 for _ in range(N+1)]
    
    for i in range(10): dp[0][i] = i
    
    # dp[i][j] i: 숫자나사 순서 j: 총 왼쪽으로 돌린 횟수 dp[i][j]: 총 회전 수
    
    for i in range(1, N+1):
        for j in range(10):
            for k in range(10):
                l = (j - k + 10) % 10
                cur_n = (cur[i-1] + j) % 10
                diff = (cur_n - tar[i-1] + 10) % 10
                
                if dp[i-1][k] + diff + l < dp[i][j]:
                    dp[i][j] = dp[i-1][k] + diff + l
                    trace[i][j] = k

    ans = []
    min_val = min(dp[-1])
    print(min_val)
    
    cur_idx = dp[-1].index(min_val)
    
    ans.append(cur_idx)
    for idx in range(N, 1, -1):
        cur_idx = trace[idx][cur_idx]
        ans.append(cur_idx)
    
    acc = 0
    idx = 0
    while ans:
        a = ans.pop()
        cur_n = (cur[idx] + acc) % 10
        print(idx+1, tar[idx] - cur_n)
        acc = a
        idx += 1
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()