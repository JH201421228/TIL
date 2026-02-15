import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def calc1(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            temp[i][j] = origin[N-1-i][j]

    return temp


def calc2(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            temp[i][j] = origin[i][M-1-j]
    
    return temp


def calc3(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * N for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            temp[i][j] = origin[N-1-j][i]

    return temp


def calc4(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * N for _ in range(M)]
    
    for i in range(M):
        for j in range(N):
            temp[i][j] = origin[j][M-1-i]

    return temp


def calc5(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * M for _ in range(N)]
    
    mid_N, mid_M = N>>1, M>>1
    
    for i in range(N):
        for j in range(M):
            if i < mid_N:
                if j < mid_M:
                    temp[i][j+mid_M] = origin[i][j]
                else:
                    temp[i+mid_N][j] = origin[i][j]
            else:
                if j < mid_M:
                    temp[i-mid_N][j] = origin[i][j]
                else:
                    temp[i][j-mid_M] = origin[i][j]

    return temp


def calc6(origin):
    N, M = len(origin), len(origin[0])
    
    temp = [[0] * M for _ in range(N)]
    
    mid_N, mid_M = N>>1, M>>1
    
    for i in range(N):
        for j in range(M):
            if i < mid_N:
                if j < mid_M:
                    temp[i+mid_N][j] = origin[i][j]
                else:
                    temp[i][j-mid_M] = origin[i][j]
            else:
                if j < mid_M:
                    temp[i][j+mid_M] = origin[i][j]
                else:
                    temp[i-mid_N][j] = origin[i][j]

    return temp


def solve():
    N, M, R = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(N)]
    calcs = tuple(map(int, input().split()))
        
    calc_map = {1: calc1, 2: calc2, 3: calc3, 4: calc4, 5: calc5, 6: calc6}
    
    for i in calcs:
        origin = calc_map[i](origin)
        
    for o in origin:
        print(*o)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()