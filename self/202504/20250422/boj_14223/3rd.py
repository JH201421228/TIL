import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isRect(x1, x2, y1, y2):
    if abs(x1-x2) == abs(y1-y2): return True
    return False


def isInnerDot(x1, x2, y1, y2):
    xl, xr, yl, yr = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    temp = 0

    for x, y in arr:
        if xl <= x <= xr and yl <= y <= yr: temp += 1

    return temp


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

bucket = []

for i in range(N-1):
    for j in range(i+1, N):
        if isRect(arr[i][0], arr[j][0], arr[i][1], arr[j][1]):
            if isInnerDot(arr[i][0], arr[j][0], arr[i][1], arr[j][1]) >= N-2:
                bucket.append(max((abs(arr[i][0]-arr[j][0])+2), (abs(arr[i][1]-arr[j][1])+2)))

print(bucket)