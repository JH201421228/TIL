import sys, math
sys.stdin = open('input.txt')
input = sys.stdin.readline

C = float(input())
N = int(input())
problems = list(map(int, input().split()))

max_freeze = min(2, int(C // 0.99))
max_solved = max(problems)

left = 0
zero_count = 0
max_streak = 0

for right in range(N):
    if problems[right] == 0:
        zero_count += 1

    while zero_count > max_freeze:
        if problems[left] == 0:
            zero_count -= 1
        left += 1

    max_streak = max(max_streak, right - left + 1)

print(max_streak)
print(max_solved)