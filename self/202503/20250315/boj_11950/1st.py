import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
flag = [input().rstrip() for _ in range(N)]

ans = float("inf")
for i in range(1, N-1):
    for j in range(1, N-1):
        cnt = 0
        for k in range(1, N-1):
            if i+j+k != N:
                continue

            for idx in range(i):
                for c in flag[idx]:
                    if c != 'W': cnt += 1

            for idx in range(i, i+j):
                for c in flag[idx]:
                    if c != 'B': cnt += 1

            for idx in range(i+j, N):
                for c in flag[idx]:
                    if c != 'R': cnt += 1

            ans = min(cnt, ans)

print(ans)