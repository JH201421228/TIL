import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    times = [tuple(map(int, input().split())) for _ in range(N)]
    state = [0] * 1_000_002

    for s, e, in times:
        state[s] += 1
        state[e+1] -= 1

    for t in range(1, 1_000_002):
        state[t] += state[t-1]

    Q = int(input())
    Qs = list(map(int, input().split()))

    for q in Qs:
        print(state[q])

    return


if __name__ == "__main__":
    solve()