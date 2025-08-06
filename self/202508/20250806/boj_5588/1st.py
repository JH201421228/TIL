import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(s, e, ti, tj, ms, ns, midx, length, oi, oj):


    for idx in range(s, e):
        if ns[idx] == (ti, tj):
            if midx+1 == length: return True
            return find(idx+1, e, ms[midx+1][0]+oi, ms[midx+1][1]+oj, ms, ns, midx+1, length, oi, oj)
    else:
        return False



def solve():
    M = int(input())
    ms = [tuple(map(int, input().split())) for _ in range(M)]
    ms.sort()

    N = int(input())
    ns = [tuple(map(int, input().split())) for _ in range(N)]
    ns.sort()

    for idx in range(N):
        oi, oj = ns[idx][0] - ms[0][0], ns[idx][1] - ms[0][1]
        if find(idx+1, N, ms[1][0]+oi, ms[1][1]+oj, ms, ns, 1, M, oi, oj):
            print(oi, oj)
            break

    return


if __name__ == "__main__":
    solve()