import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def binary_search(n):
    s, e = 0, N-1

    while s <= e:
        mid = (s+e) >> 1

        if strengths[mid] < n:
            s = mid+1
        else:
            e = mid-1

    return s


N, M = map(int, input().split())
titles = []
strengths = []

for _ in range(N):
    t, s = map(str, input().split())
    titles.append(t)
    strengths.append(int(s))

for _ in range(M):
    print(titles[binary_search(int(input()))])