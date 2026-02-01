import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(cur, i, j, V1, V2, V3):
    if i >= 9:
        for c in cur:
            print(''.join(map(str, c)))
            
        exit(0)
    
    if j >= 9: 
        dfs(cur, i+1, 0, V1, V2, V3)
        return
    

    if cur[i][j]:
        dfs(cur, i, j+1, V1, V2, V3)
        return
    
    for n in range(1, 10):
        if not V1[i][n-1] and not V2[j][n-1] and not V3[3*(i//3)+(j//3)][n-1]:
            V1[i][n-1] = 1
            V2[j][n-1] = 1
            V3[3*(i//3)+(j//3)][n-1] = 1
            cur[i][j] = n
            
            dfs(cur, i, j+1, V1, V2, V3)
    
            V1[i][n-1] = 0
            V2[j][n-1] = 0
            V3[3*(i//3)+(j//3)][n-1] = 0
            cur[i][j] = 0
    
    return 


def solve():
    V_vertical = [[0] * 9 for _ in range(9)]
    V_horizontal = [[0] * 9 for _ in range(9)]
    V_patch = [[0] * 9 for _ in range(9)]
    
    cur = [list(map(int, input().rstrip())) for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if cur[i][j]:
                V_vertical[i][cur[i][j]-1] = 1
                V_horizontal[j][cur[i][j]-1] = 1
                V_patch[3*(i//3)+(j//3)][cur[i][j]-1] = 1
    

    dfs(cur, 0, 0, V_vertical, V_horizontal, V_patch)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()