import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n, V, C, G):
    for x in G[n]:
        if V[x]: continue
        V[x] = 1

        if not C[x] or B(C[x], V, C, G):
            C[x] = n
            return True

    return False


def solve():
    N = int(input())
    names = list(input().rstrip().split())

    names_to_num = {}

    for n in range(N):
        names_to_num[names[n]] = n+1

    G = [[] for _ in range(N+1)]
    state = [0] * (N+1)
    for _ in range(int(input())):
        temp = list(input().rstrip().split())
        for name in temp[2:]:
            state[names_to_num[name]] = max(state[names_to_num[name]], int(temp[1]))

    C = [0] * (N+1)
    for n in range(1, N+1):
        V = [0] * (N+1)
        B(n, V, C, G)

    print(names_to_num)
    print(C)
    print(G)

    return


if __name__ == "__main__":
    solve()