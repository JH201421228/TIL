import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    jewelries = [tuple(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]

    jewelries.sort()
    bags.sort()

    n = 0
    ans = 0
    pq = []
    for k in range(K):
        while n < N and jewelries[n][0] <= bags[k]:
            heapq.heappush(pq, -jewelries[n][1])
            n += 1

        if pq:
            ans -= heapq.heappop(pq)

    print(ans)

    return


if __name__ == "__main__":
    main()