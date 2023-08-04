# 풍선팡
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for test_case in range(Test_Case):
    N, M = map(int, input().split())
    balloon_list = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    max_val = 0
    for x in range(N):
        for y in range(M):
            total = balloon_list[x][y]
            for i in range(1, balloon_list[x][y] + 1):
                for delta in range(4):
                    if 0 <= x + dx[delta] * i < N and 0 <= y + dy[delta] * i < M:
                        total += balloon_list[x + dx[delta] * i][y + dy[delta] * i]
            if total > max_val:
                max_val = total

    print(f'#{test_case + 1} {max_val}')