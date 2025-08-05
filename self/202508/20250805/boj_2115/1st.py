import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def count_picture(gallery, n, m, di, dj):
    res = 0

    for i in range(1, n-1):
        tmp = 0
        for j in range(1, m-1):
            if gallery[i][j] == '.' and gallery[i+di][j+dj] == 'X':
                tmp += 1
            else:
                res += tmp // 2
                tmp = 0

        res += tmp // 2

    return res


def solve():
    M, N = map(int, input().split())
    gallery = [list(input().rstrip()) for _ in range(M)]
    gallery_T = [[] for _ in range(N)]
    for j in range(N):
        for i in range(M):
            gallery_T[j].append(gallery[i][j])

    res = 0

    res += count_picture(gallery, M, N, 1, 0)
    res += count_picture(gallery, M, N, -1, 0)
    res += count_picture(gallery_T, N, M, 1, 0)
    res += count_picture(gallery_T, N, M, -1, 0)

    print(res)

    return


if __name__ == "__main__":
    solve()