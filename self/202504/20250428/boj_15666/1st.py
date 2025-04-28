import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(pre, depth):
    if depth > M:
        print(*temp)
        return

    for idx in range(pre, len(arr)):
        temp.append(arr[idx])
        solve(idx, depth+1)
        temp.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_set = set(arr)
arr = list(arr_set)
arr.sort()
temp = []


if __name__ == "__main__":
    solve(0, 1)
