import sys
sys.stdin = open('input.txt')

def why_do_this(N, M, arr, start):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, N+1):
        ans.append(i)
        why_do_this(N, M, ans, i)
        ans.pop()

N, M = map(int, input().split())

ans = []
start = 1
why_do_this(N, M, ans, start)