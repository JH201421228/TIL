import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def get_value(N, cur, ex, n):
    res = (N**2 + N) // 2
    res += cur * N
    res -= ex
    res -= cur * n
    return res


def solve():
    N, Q = map(int, input().split())

    V_r = [0] * (N+1)
    V_c = [0] * (N+1)
    ex_r = 0
    n_r = 0
    ex_c = 0
    n_c = 0

    for _ in range(Q):
        query = list(input().rstrip().split())

        if query[0] == 'R':
            if not V_r[int(query[1])]:
                V_r[int(query[1])] = 1
                print(get_value(N, int(query[1]), ex_r, n_r))
                ex_c += int(query[1])
                n_c += 1
            else:
                print(0)
        else:
            if not V_c[int(query[1])]:
                V_c[int(query[1])] = 1
                print(get_value(N, int(query[1]), ex_c, n_c))
                ex_r += int(query[1])
                n_r += 1
            else:
                print(0)

    return


if __name__ == "__main__":
    solve()