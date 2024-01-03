import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for t in range(int(input())):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    temp += fly_list[x][y]
            if temp > ans:
                ans = temp
    print(f'#{t+1} {ans}')
