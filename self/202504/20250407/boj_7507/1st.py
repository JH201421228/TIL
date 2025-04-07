import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

for z in range(int(input())):
    q = []
    for _ in range(int(input())):
        heapq.heappush(q, tuple(map(int, input().split())))

    ans = 0
    cur = 0
    pre_s, pre_e = 0, 0
    while q:
        d, s, e = heapq.heappop(q)

        if cur != d:
            cur = d
            pre_e = e
            ans += 1
            continue

        if s >= pre_e:
            ans += 1
            pre_e = e
        elif e < pre_e:
            pre_e = e

    print(f"Scenario #{z+1}:")
    print(ans)
    print()