import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


num = int(input())
meeting_info = [list(map(int, input().split())) for _ in range(num)]
meeting_info.sort()
# print(meeting_info)
meeting_info.sort(key=lambda x:x[1])
# print(meeting_info)
ans = 0
pre_end = 0
for start, end in meeting_info:
    if start >= pre_end:
        ans += 1
        pre_end = end
print(ans)