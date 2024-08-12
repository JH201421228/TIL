import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(200_000)


def area(s, e):
    if s == e:
        return heights[s]

    mid = (s+e) // 2
    l = mid-1
    r = mid+1
    ans = heights[mid]
    h = heights[mid]

    while (s <= l or r <= e):
        if (s > l):
            h = min(h, heights[r])
            r += 1
        elif (e < r):
            h = min(h, heights[l])
            l -= 1
        elif (heights[l] >= heights[r]):
            h = min(h, heights[l])
            l -= 1
        elif (heights[l] < heights[r]):
            h = min(h, heights[r])
            r += 1

        ans = max(ans, h*(r-l-1))

    return max(ans, area(s, mid), area(mid+1, e))


N = int(input())
heights = []
for _ in range(N):
    heights.append(int(input()))

print(area(0, N-1))