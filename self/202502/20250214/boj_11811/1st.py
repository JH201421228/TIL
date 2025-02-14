import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

ans_list = []

for _ in range(N):
    temp = list(map(int, input().split()))
    ans = 0

    for t in temp:
        ans |= t

    ans_list.append(ans)

print(*ans_list)