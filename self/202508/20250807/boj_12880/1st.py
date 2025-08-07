import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(v, l, r, flag, g, n, chk, cnt):
    cnt[0] += 1
    chk[v] = True

    for i in range(1, n + 1):
        if flag:
            if not chk[i] and l <= g[v][i] <= r:
                dfs(i, l, r, flag, g, n, chk, cnt)
        else:
            if not chk[i] and l <= g[i][v] <= r:
                dfs(i, l, r, flag, g, n, chk, cnt)


def valid(l, r, g, n):
    chk = [False] * (n + 1)
    cnt = [0]
    dfs(1, l, r, False, g, n, chk, cnt)

    if cnt[0] != n:
        return False

    chk = [False] * (n + 1)
    cnt = [0]
    dfs(1, l, r, True, g, n, chk, cnt)

    return cnt[0] == n


def main():
    n = int(input())

    g = [[0] * (n + 1) for _ in range(n + 1)]
    comp = []

    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(n):
            g[i][j + 1] = row[j]
            comp.append(row[j])

    comp = sorted(list(set(comp)))

    mn = float('inf')
    l = 0

    for r in range(len(comp)):
        while l <= r:
            if valid(comp[l], comp[r], g, n):
                mn = min(mn, comp[r] - comp[l])
                l += 1
            else:
                break

    print(mn)


if __name__ == "__main__":
    main()