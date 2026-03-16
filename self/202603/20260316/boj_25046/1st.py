import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    arr = [0] * N
    
    for i in range(N):
        for j in range(N):
            arr[j] += board[i][j]
    
    ans = -float("inf")
    
    for i in range(1<<N):
        cur = []
        for j in range(N):
            if i & (1<<j): cur.append(j)
        
        res = 0
        for jdx in range(N):
            tmp = 0
            for idx in cur:
                tmp += board[idx][jdx]
            res += min(tmp, arr[jdx]-tmp)
        
        ans = max(ans, res)
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()