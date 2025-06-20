import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    _B = [B[0]]

    for idx in range(1, M):
        _B.append(B[idx]+_B[-1])

    state = [0] * 7
    for idx in range(N):
        state[A[idx] % 7] = 1

    add = 0
    for idx in range(M):
        add += B[idx]
        temp = [*state]
        for n in range(7):
            if not (add + n) % 7:
                temp[n] = 0

        if not sum(temp):
            add -= B[idx]
            continue
        state = temp

    ans = []
    MOD = 1_000_000_007

    for idx in range(N):
        if state[A[idx] % 7]: ans.append((A[idx]+add) % MOD)

    print(len(ans))
    print(*ans)

    return


if __name__ == "__main__":
    solve()