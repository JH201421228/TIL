import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(depth):
    if depth >= M:
        print(*temp)
        return

    for idx in range(N):
        if not V[idx]:
            temp.append(arr[idx])
            V[idx] = 1
            solve(depth+1)
            temp.pop()
            V[idx] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
V = [0] * N
temp = []

solve(0)