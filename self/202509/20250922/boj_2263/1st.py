import sys
sys.setrecursionlimit(100_000)
sys.stdin = open('input.txt')
input = sys.stdin.readline


def root_node(ino, posto, i_s, i_e, p_s, p_e):
    if i_s > i_e or p_s > p_e:
        return

    print(mid := posto[p_e], end=' ')

    if i_s == i_e:
        return

    for i in range(i_s, i_e+1):
        if ino[i] == mid:
            root_node(ino, posto, i_s, i-1, p_s, p_s+(i-i_s-1))
            root_node(ino, posto, i+1, i_e, p_s+(i-i_s), p_e-1)
            return

    return


def solve(N):
    ino = list(map(int, input().split()))
    posto = list(map(int, input().split()))

    root_node(ino, posto, 0, N-1, 0, N-1)

    return


def main():
    solve(int(input()))
    return


if __name__ == "__main__":
    main()