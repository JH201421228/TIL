import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def cal(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (mat1[i][k] * mat2[k][j]) % MOD
                res[i][j] %= MOD
                
    return res


def recur(n, mat):
    res = [[1, 0], [0, 1]]
    
    while n:
        if n%2:
            res = cal(res, mat)
        mat = cal(mat, mat)
        n //= 2
        
    return res
            

def solve():
    N = int(input())
    
    if N%2:
        print(0)
        return
    
    res = [[4, -1], [1, 0]]
    res = recur(N//2, res)
    print((res[0][0] + res[0][1])%MOD)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()