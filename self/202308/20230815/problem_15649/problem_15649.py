import sys
sys.stdin = open('input.txt')

def combi(N, M, arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            combi(N, M, ans)
            ans.pop()


N, M = map(int, input().split())
ans = []
combi(N, M, ans)