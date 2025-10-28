import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    counter = dict()

    for idx in range(N):
        cur = arr[idx]
        counter[cur] = counter.get(cur, 0) + 1
    
    ans = [0] * N

    S = []

    for idx in range(N):
        cur = arr[N-1-idx]

        if not S:
            ans[N-1-idx] = -1

        else:

            while S and S[-1][0] <= counter[cur]:
                S.pop()

            if S:
                ans[N-1-idx] = arr[N-1-S[-1][1]]
            else:
                ans[N-1-idx] = -1

        S.append((counter[cur], idx))
        
    print(*ans)


    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()