import sys
sys.stdin = open('input.txt')

def all(N, M, arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        ans.append(i)
        all(N, M, ans)
        ans.pop()

N, M = map(int, input().split())
ans = []
all(N, M, ans)