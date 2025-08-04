import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    L, N, K = map(int, input().split())
    stations = list(map(int, input().split()))
    stations.append(L)

    s = stations[0]
    for idx in range(N):
        s = max(s, stations[idx+1] - stations[idx])

    e = L

    while s <= e:
        mid = (s+e) >> 1

        cnt = 0
        n = mid

        for idx in range(N+1):
            dist = stations[idx] - stations[idx-1] if idx > 0 else stations[idx]

            if n < dist:
                n = mid - dist
                cnt += 1
            else:
                n -= dist

        if cnt > K: s = mid+1
        else: e = mid-1


    print(s)

    return


if __name__ == "__main__":
    solve()