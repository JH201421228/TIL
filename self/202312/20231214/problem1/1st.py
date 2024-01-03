import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for t in range(int(input())):
    N, M = map(int, input().split())
    paper_flower = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(M):
            val = paper_flower[i][j]
            temp = paper_flower[i][j]

            for di, dj in delta:
                for multi in range(1, val+1):
                    if 0 <= i+di*multi < N and 0 <= j+dj*multi < M:
                        temp += paper_flower[i+di*multi][j+dj*multi]

            ans = max(ans, temp)

    print(f'#{t+1} {ans}')