import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
scores = list(map(int, input().split()))

def find_group(x):
    group_num = 0
    temp = 0
    for idx in range(N):
        temp += scores[idx]
        if temp >= x:
            temp = 0
            group_num += 1
    return group_num

start, end = 0, sum(scores)

while start <= end:
    mid = (start + end) >> 1
    if find_group(mid) < K:
        end = mid - 1
    else:
        start = mid + 1
print(end)
