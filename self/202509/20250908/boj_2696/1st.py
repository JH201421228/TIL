import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    M = int(input())
    arr = []
    for _ in range((M-1)//10 + 1):
        arr.extend(map(int, input().split()))

    cur = 0

    acs = [float('inf')]
    desc = [float('inf')]
    acs_len = 1
    desc_len = 1

    ans = []

    while cur < M:
        n = arr[cur]

        if acs_len == desc_len:
            heapq.heappush(desc, -n)
            acs_n = heapq.heappop(acs)
            desc_n = -heapq.heappop(desc)

            acs_n, desc_n = max(acs_n, desc_n), min(acs_n, desc_n)

            heapq.heappush(acs, acs_n)
            heapq.heappush(desc, -desc_n)

            ans.append(desc_n)
            desc_len += 1

        else:
            desc_n = -heapq.heappop(desc)

            acs_n, desc_n = max(n, desc_n), min(n, desc_n)

            heapq.heappush(acs, acs_n)
            heapq.heappush(desc, -desc_n)

            acs_len += 1

        cur += 1

    length = len(ans)
    print(length)
    for idx in range((len(ans)-1)//10 + 1):
        print(*ans[idx*10:min((idx*10+10), length)])

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()