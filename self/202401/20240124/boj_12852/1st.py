import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(30000)


def dfs(val, arr):

    if val == N:
        print(len(arr)-1)
        arr.sort(reverse=True)
        print(*arr)
        exit(0)


    if val * 3 <= N:
        dfs(val*3, arr+[val*3])
    if val * 2 <= N:
        dfs(val*2, arr+[val*2])
    if val + 1 <= N:
        dfs(val+1, arr+[val+1])

    return


N = int(input())
dfs(1, [1])