import sys
sys.stdin = open('input.txt')

def permu(N, M, arr, start):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            permu(N, M, ans, i+1)
            index = ans.pop()

N, M = map(int, input().split())
ans = []
start = 1
permu(N, M, ans, start)