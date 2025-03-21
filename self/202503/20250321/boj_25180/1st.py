import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

cnt = (N // 18) * 2

if N % 18:
    if N % 18 < 10:
        cnt += 1
    else:
        if (N % 18) % 2:
            cnt += 3
        else:
            cnt += 2

print(cnt)