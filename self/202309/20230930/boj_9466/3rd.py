import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(150000)

def holiday(n):
    visited[n] = 1
    check.append(n)
    next = stu_list[n]

    if visited[next]:
        if next in check:
            ans.extend(check[check.index(next):])
        return
    else:
        holiday(next)


for _ in range(int(input())):
    N = int(input())
    stu_list = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    ans = []

    for idx in range(1, N+1):
        if not visited[idx]:
            check = []
            holiday(idx)
    print(N - len(ans))