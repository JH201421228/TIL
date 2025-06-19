import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M, S, T = map(int, input().split())
    arr = [[float("inf")] * N for _ in range(N)]
    for i in range(N): arr[i][i] = 0

    for _ in range(M):
        u, v, d = map(int, input().split())
        arr[u-1][v-1] = min(arr[u-1][v-1], d)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

    for _ in range(int(input())):
        a, b, c, d, e, f = map(int, input().split())
        ans = [arr[S-1][T-1]]
        ans.append(arr[S-1][a-1] + arr[b-1][T-1] + c)
        ans.append(arr[S-1][d-1] + arr[e-1][T-1] + f)
        ans.append(arr[S-1][a-1] + arr[b-1][d-1] + arr[e-1][T-1] + c + f)
        ans.append(arr[S-1][d-1] + arr[e-1][a-1] + arr[b-1][T-1] + c + f)

        if min(ans) == float("inf"): print(-1)
        else: print(min(ans))

    return


if __name__ == "__main__":
    solve()